#tipe data skalar => tipe data sederhana
from typing import List

anak1 = 'putu'
anak2 = 'kadek'
anak3 = 'komang'
anak4 = 'ketut'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#tipe data list/daftar/array
anak: List[str] = ['putu', 'kadek', 'komang', 'ketut']
print(anak)
anak.append('limo')
print(anak)

print('\nsapa anak ke-2')
print(f'hai {anak [1]}')

print('\nsapa semua anak')
for a in anak :
    print(f'hai {a}')

print('\nsapa semua anak: cara ribet')
for a in range(0,len(anak)):
    print(f'{a+1}. hai {anak[a]}')
    