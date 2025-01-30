# operator membership

"""
Operator in digunakan untuk mengecek apakah suatu nilai merupakan bagian dari data kolektif atau tidak.

Operator ini bisa dipergunakan pada semua tipe data kolektif seperti dictionary, set, tuple, dan list.
Selain itu, operator in juga bisa digunakan pada string untuk pengecekan substring
"""

sample_list = [2, 3, 4]
is_3_exists = 3 in sample_list
print(is_3_exists)
# output ➜ True

sample_tuple = ("hello", "python")
is_hello_exists = "hello" in sample_tuple
print(is_hello_exists)
# output ➜ True

sample_dict = { "nama": "noval", "age": 12 }
is_key_nama_exists = "nama" in sample_dict
print(is_key_nama_exists)
# output ➜ True

sample_set = { "sesuk", "preiiii" }
is_prei = "preiiii" in sample_set
print(is_prei)
# output ➜ True

text = 'Hello world'
is_substring_exists = 'orl' in text
print(is_substring_exists)
# output ➜ True


# Operator in jika diterapkan pada tipe dictionary, yang di-check adalah key-nya bukan value-nya.