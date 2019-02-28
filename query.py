queries = [
	'select status from dirawat;',
	'select no_inventaris, nama, jenis from fasilitas;',
	'select no_inventaris, tgl_lahir, jenis from pegawai, fasilitas;',
	'select no_inventaris, nama, jenis from;',
	'select no_inventaris, nama, jenis from dirawat;',
	'select no_inventaris,tgl_lahir,jenis from pegawai,fasilitas;',
	'select * from pegawai,fasilitas;',
	'select p.nama, f.nama from pegawai p join dirawat r using (no_ktp) join fasilitas f using (no_inventaris);',
]