# operator identity

"""
Operator is memiliki kemiripan dengan operator logika ==,
perbedaannya pada operator is yang dibandingkan bukan nilai, melainkan identitas atau ID-nya.

Bisa saja ada 2 variabel bernilai sama tapi identitasnya berbeda.
"""

num_1 = 100001
num_2 = 100001

res = num_1 is num_2
print("num_1 is num_2 =", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))

"""
Pengecekan nilai kosong (atau None) dianjurkan untuk selalu dilakukan menggunakan operator is,
dan menghindari penggunaan operator ==.

Hal ini karena operator is membandingkan identitas data dan identitas data None selalu valid.
Sedangkan operator == perbandingannya dilakukan dengan via special method __eq__()
yang default method tersebut bisa di-override isinya.
"""