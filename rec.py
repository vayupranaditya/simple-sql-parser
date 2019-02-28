tables = {
	'pegawai' : ['no_ktp', 'nama', 'tgl_lahir', 'gender', 'pendidikan'],
	'dirawat' : ['tgl_dirawat', 'status', 'periode', 'pegawai_no_ktp', 'fasilitas_no_inventaris'],
	'fasilitas' : ['no_inventaris', 'nama', 'jenis', 'tgl_dibeli', 'pemakaian']
}

queries = [
	'select status from dirawat;',
	'select no_ktp, nama, gender from pegawai;',
	'select no_inventaris, nama, jenis from fasilitas;',
	'select no_inventaris, nama, jenis from pegawai;',
	'select no_inventaris, nama, jenis from ;',
	'select no_inventaris, nama, jenis from;',
]

def check(query, tables):
	query = query.lower()
	if ((query.find('select ') == 0) and (query.find(' from ') > query.find('select ')) and (query[-1] == ';')):
		query = query[7:-1]
		colTab = query.split(' from ')
		cols = getCols(colTab[0])
		tabs = getTabs(colTab[1])
		if (False not in cols and False not in tabs):
			print(cols)
			print(tabs)
			print(checkExistance(cols, tabs, tables))
		elif (False in cols):
			print(cols)
		elif (False in tabs):
			print(tabs)
	else:
		print((False, 'syntax error'))

def checkCol(col, tabs, tables):
	for tab in tabs:
		if (col in tables[tab]):
			return True
	return False

def checkExistance(cols, tabs, tables):
	for col in cols:
		if not checkCol(col, tabs, tables):
			return False, 'column ' + col + ' is not found.'
	else:
		return True

def getCols(cols):
	cols = cols.split(',')
	for col in cols:
		if (len(col) == 0):
			return False, 'syntax error';
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

for query in queries:
	check(query, tables)
	print()