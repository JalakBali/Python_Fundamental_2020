#tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
#KVP = Key Value Pair
#dictionary = kamus

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}
print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\nData yg dikirimkan oleh server gojek, utk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '20200627',
    'driver_list' : [
        {'nama':'putu','jarak':10},
        {'nama':'kadek','jarak' : 20},
        {'nama':'komang','jarak':30},
        {'nama':'ketut','jarak':40}
    ]
}
print(data_dari_server_gojek)
print(f"\ndriver disekitar sini{data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #2 {data_dari_server_gojek['driver_list'][1]}")
print(f"driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"driver #4 {data_dari_server_gojek['driver_list'][3]}")

print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
