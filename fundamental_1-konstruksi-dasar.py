# Konstruksi Dasar Python
# sequential : Eksekusi berurutan
print('hello world')
print('by Sugiharto Budidarman')
print('tanggal 26 Juni 2020')
print('-' * 10)

#percabangan : Eksukusi terpilih
ingin_cepat = False
if ingin_cepat :
    print('jalan lurus aja bro')
else :
    print('jalan lain sono')

#perulangan
jumlah_anak = 4

for index_anak in range (1,jumlah_anak + 1) : #jumlah perulangan = 5 - 1 = 4
    print(f'halo anak # {index_anak}')
