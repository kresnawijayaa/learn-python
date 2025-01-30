# operator bitwise

# Operator AND (&)
# Menghasilkan 1 hanya jika kedua bit bernilai 1, selain itu hasilnya 0.
x = 6  # 0000 0110 (biner)
y = 4  # 0000 0100 (biner)
hasil = x & y  # 0000 0100 (4 dalam desimal)
print(hasil)  # Output: 4

# Operator OR (|)
# Menghasilkan 1 jika salah satu bit bernilai 1.
x = 6  # 0000 0110
y = 4  # 0000 0100
hasil = x | y  # 0000 0110 (6 dalam desimal)
print(hasil)  # Output: 6

# Operator NOT (~)
# Membalik setiap bit (bit 1 menjadi 0, dan sebaliknya).
# Karena Python menggunakan bilangan bertanda (signed integer), hasilnya adalah -(n+1).
x = 10  # 0000 1010
hasil = ~x  # -(10+1) = -11
print(hasil)  # Output: -11

# perator XOR (^)
# Menghasilkan 1 jika kedua bit berbeda, jika sama hasilnya 0.
x = 6  # 0000 0110
y = 4  # 0000 0100
hasil = x ^ y  # 0000 0010 (2 dalam desimal)
print(hasil)  # Output: 2

# Operator Right Shift (>>)
# Menggeser bit ke kanan sebanyak n posisi (membagi dengan 2^n).
x = 8  # 0000 1000
hasil = x >> 2  # 0000 0010 (2 dalam desimal)
print(hasil)  # Output: 2

# Operator Left Shift (<<)
# Menggeser bit ke kiri sebanyak n posisi (mengalikan dengan 2^n).
x = 5  # 0000 0101
hasil = x << 2  # 0001 0100 (20 dalam desimal)
print(hasil)  # Output: 20