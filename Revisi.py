# Input jumlah angka (tidak ada batasan sesuai revisi)
jml_angka = int(input("Masukkan jumlah angka yang ingin diinput: "))

# Input angka (boleh desimal sesuai revisi)
angka = [float(input(f"Masukkan angka ke-{i+1}: ")) for i in range(jml_angka)]

# Tampilkan sebelum urut
print(f"\nSebelum diurutkan:\n{angka}")

# Bubble sort 
for i in range(1, jml_angka + 1):
    for j in range(jml_angka - i):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

# Tampilkan setelah urut
print(f"\nSesudah diurutkan:\n{angka}")

# Bagian Revisi
terbesar = angka[-1]
terkecil = angka[0]
rata_rata = sum(angka) / len(angka)

print(f"\nAngka terbesar : {terbesar}")
print(f"Angka terkecil : {terkecil}")
print(f"Rata-rata      : {rata_rata:.2f}")