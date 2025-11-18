# Input pembatas
jml_angka = int(input("Masukkan jumlah angka(5-10) = "))
while jml_angka > 10 or jml_angka < 5:
    jml_angka = int(input("Masukkan jumlah angka(5-10) = "))

# Input angka
angka = [int(input(f"Masukkan angka ke-{i + 1} = ")) for i in range(jml_angka)]

# Tampilkan sebelum urut
print(f"\nSebelum: \n{angka}")

# Bubble sort
for i in range(1, jml_angka + 1):
    for j in range(jml_angka - i):
        if angka[j] > angka[j + 1]:
            k = angka[j]
            angka[j] = angka[j + 1]
            angka[j + 1] = k

# Tampilkan sesudah urut
print(f"\nSesudah: \n{angka}")