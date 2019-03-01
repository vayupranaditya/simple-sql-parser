import re
import os
os.system('cls')

tables = {
	'pegawai' : ['no_ktp', 'nama', 'tgl_lahir', 'gender', 'pendidikan'],
	'dirawat' : ['tgl_dirawat', 'status', 'periode', 'pegawai_no_ktp', 'fasilitas_no_inventaris'],
	'fasilitas' : ['no_inventaris', 'nama', 'jenis', 'tgl_dibeli', 'pemakaian']
}

queries = [
	'select status from dirawat;',
	'select no_inventaris, nama, jenis from fasilitas;',
	'select no_inventaris, tgl_lahir, jenis from pegawai, fasilitas;',
	# 'select no_inventaris, nama, jenis from;',
	'select no_inventaris, nama, jenis from dirawat;',
	'select no_inventaris,tgl_lahir,jenis from pegawai,fasilitas;',
	# 'select * from pegawai,fasilitas f g v;',
	'select p.nama, f.nama from pegawai p join dirawat r using (no_ktp) join fasilitas f using (no_inventaris);',
]

# all get returns {status: <status>, raw: <raw>, data: <data>}
# status: True | False
# raw: raw substring
# data: formatted substring if status == True | error status if status == False

# def base(query):
# 	query = query.lower()
# 	if (query[0:7] == 'select '):
# 		# get columns. delimit using ' from '
# 		cols = getCols(query)
# 		# if False not in cols:
# 			# if query.find(' from ') != -1:
# 				# get tables (first table if using join). delimit using 'join' or ';'
# 				tabs = getTabs()
# 				if False not in tabs:
# 					if query.find(' join ') != -1:
# 						# get all join. getJoins may be recursive
# 						joins = getJoins()
# 						if False not in joins:
# 							# what to do
# 						if query.find(';') != -1:
# 							# what to do
# 						else:
# 							# what to do
# 					else:
# 						# no join
# 				else:
# 					return {
# 						'status' : False,
# 						'raw' : tabs['raw'],
# 						'data' : tabs['data']
# 					}
# 			else:
# 				return {
# 					'status' : False,
# 					'raw' : query,
# 					'data' : 'syntax error'
# 				}
# 		else:
# 			return {
# 				'status' : False,
# 				'raw' : cols['raw'],
# 				'data' : cols['data']
# 			}
# 	else:
# 		return {
# 			'status' : False,
# 			'raw' : query,
# 			'data' : 'syntax error'
# 		}

def base(query):
	i = 0
	join = []
	qu = query
	queries = query.split(' ')
	if queries[i] == 'select':
		cols = getCols(query)
		if False not in cols:
			print('COLS', cols)
			while queries[i] != 'from' and i < len(queries)-1:
				i+=1
			if queries[i] != queries[-1]:
				tabs = getTabs(query)
				if False not in tabs:
					print('TABS', tabs)
					qu = qu[qu.find(' join '):]
					for q in queries:
						if q == 'join':
							qu = qu[qu.find(' join ')+1:]
							# print(qu)
							join.append(getJoin(qu))
					print(join)

def getJoin(query):
	query = query[5:query.find(')')+1]
	queries = query.split(' using ')
	if len(re.findall('. .', queries[0])) != 1:
		return {
			'status' : False,
			'raw' : query,
			'data' : 'table syntax error'
		}
	else:
		tabs = queries[0].split(' ')
		tab = tabs[0]
		if len(tabs) > 1:
			identifier = tabs[1]
			return {
				'status' : True,
				'raw' : query,
				'data' : {
					'join' : {
						'identifier' : identifier,
						'table' : tab,
						'key' : queries[1][1:-1]
					}
				}
			}
		else:
			return {
				'status' : True,
				'raw' : query,
				'data' : {
					'table' : tab,
					'key' : queries[1][1:-1]
				}
			}



def getTabs(query):
	query = query[query.find(' from ')+len(' from '):]
	if query.find(' join ') != -1:
		query = query[:query.find(' join ')]
		if (query.replace(' ','') == ''):
			return {
				'status' : False,
				'raw' : query,
				'data' : 'no table selected'
			}
		else:
			tabs = query.split(',')
			for i in range(0, len(tabs)):
				print(re.findall('. .+ ', tabs[i]))
				if len(re.findall('. . . .', tabs[i])) > 1:
					return {
						'status' : False,
						'raw' : query,
						'data' : 'table syntax error'
					}
				if tabs[i][0] == ' ':
					tabs[i] = tabs[i][1:]
				if tabs[i][-1] == ' ':
					tabs[i] = tabs[i][:-1]
			return {
				'status' : True,
				'raw' : query,
				'data' : {'join' : tabs}
			}
	else:
		# not using join
		tabs = query.split(',')
		for i in range(0, len(tabs)):
			print(re.findall('. .', tabs[i]))
			if len(re.findall('. .', tabs[i])) > 1:
				return {
					'status' : False,
					'raw' : query,
					'data' : 'table syntax error'
				}
			if tabs[i][0] == ' ':
				tabs[i] = tabs[i][1:]
			if tabs[i][-1] == ' ':
				tabs[i] = tabs[i][:-1]
		return {
			'status' : True,
			'raw' : query,
			'data' : tabs
		}

def getCols(query):
	query = query[7:query.find(' from ')]
	if (query == ''):
		return {
			'status' : False,
			'raw' : query,
			'data' : 'no column selected'
		}
	elif (query == '*'):
		return {
			'status' : True,
			'raw' : query,
			'data' : query
		}
	else:
		# parse by comma
		cols = query.split(',')
		# check if any space separated column name
		for i in range(0, len(cols)):
			if re.search('. .', cols[i]):
				return {
					'status' : False,
					'raw' : query,
					'data' : 'syntax error'
				}
			cols[i] = cols[i].replace(' ','')
	return {
		'status' : True,
		'raw' : query,
		'data' : cols
	}




for query in queries:
	print()
	print(query)
	# print(getCols(query))
	# print(getTabs(query))
	# print(getJoin(query))
	print(base(query))
	print()