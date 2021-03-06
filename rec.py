# python 3.6

# IF-41-07
# I Gusti Bagus Vayupranaditya Putraadinatha 1301174029
# Angela Marpaung 1301174111
# Beladina Elfitri 1301174046
# Shindy Trimaria Laxmi 1301170092
import json
import re
import os
os.system('cls')
print("""IF-41-07
I Gusti Bagus Vayupranaditya Putraadinatha 1301174029
Angela Marpaung 1301174111
Beladina Elfitri 1301174046
Shindy Trimaria Laxmi 1301170092
""")

filename = 'data_dictionary.txt'
file = open(filename, 'r')
fileContent = file.read()
fileContent = fileContent.lower()
fileContent = re.sub('\n', '', fileContent)
ts = fileContent.split('#')
tables = {}
for t in ts:
	c = t.split(';')
	tables[c[0]] = c[1:]
# print(tables)

# print(json.dumps(tables))
# tables = {
# 	'pegawai' : ['no_ktp', 'nama', 'tgl_lahir', 'gender', 'pendidikan'],
# 	'dirawat' : ['tgl_dirawat', 'status', 'periode', 'pegawai_no_ktp', 'fasilitas_no_inventaris'],
# 	'fasilitas' : ['no_inventaris', 'nama', 'jenis', 'tgl_dibeli', 'pemakaian']
# }

# queries = [
# 	'select status from dirawat;',
# 	'select no_inventaris, nama, jenis from fasilitas;',
# 	'select no_inventaris, tgl_lahir, jenis from pegawai, fasilitas;',
# 	'select no_inventaris, nama, jenis from;',
# 	'select no_inventaris, nama, jenis from dirawat;',
# 	'select no_inventaris,tgl_lahir,jenis from pegawai,fasilitas;',
# 	'select * from pegawai,fasilitas;',
# 	'select p.nama, f.nama from pegawai p join dirawat r using (no_ktp) join fasilitas f using (no_inventaris);',
# ]

def check(query, tables):
	query = query.lower()
	if ((query.find('select ') == 0) and (query.find(' from ') > query.find('select ')) and (query[-1] == ';')):
		query = query[7:-1]
		colTab = query.split(' from ')
		cols = getCols(colTab[0])
		tabs = getTabs(colTab[1])
		if (False not in cols and False not in tabs):
			# print(cols)
			# print(tabs)
			print(checkExistance(cols, tabs, tables))
		elif (False in cols):
			print(cols)
		elif (False in tabs):
			print(tabs)
	else:
		print((False, 'syntax error'))

def checkCol(col, tabs, tables):
	dotIdx = col.find('.')
	if dotIdx != -1:
		prefix = col[:dotIdx]
		col = col[dotIdx+1:]
		tabPrefixIdx = tabs[0].find(' ' + prefix + ' ')
		# if (col in )
		# print('pre', tabs[0][tabPrefixIdx+1])
	for tab in tabs:
		if col in tables[tab]:
			return (True, (tab, col))
		elif col == '*':
			return (True, (tab, tables[tab]))
	return (False, 'column ' + col + 'is not found')

def checkExistance(cols, tabs, tables):
	pair = []
	for col in cols:
		colExists = checkCol(col, tabs, tables)
		# print('colExists', end=' ')
		# print(colExists)
		if colExists[0] == False:
			return False, 'column ' + col + ' is not found.'
		else:
			pair.append(colExists[1])
	return (True, groupByTable(pair))

def groupByTable(pairs):
	tabs = {}
	for pair in pairs:
		if pair[0] not in tabs:
			tabs[pair[0]] = [pair[1]]
		else:
			tabs[pair[0]].append(pair[1])
	return tabs

def getCols(cols):
	cols = cols.split(',')
	for col in cols:
		if (len(col) == 0):
			return (False, 'syntax error');
	for i in range(0, len(cols)):
		if (cols[i][0] == ' '):
			cols[i] = cols[i][1:]
	# columns got
	return cols

def getTabs(tabs):
	tabs = tabs.split(',')
	for tab in tabs:
		if (len(tab) == 0):
			return False, 'syntax error';
	for i in range(0, len(tabs)):
		if (tabs[i][0] == ' '):
			tabs[i] = tabs[i][1:]
	# tables got
	return tabs

# for query in queries:
# 	print()
# 	print(query)
# 	check(query, tables)
# 	print()
query = input('>')
check(query, tables)