# konstanta adalah variabel yang nilainya dideklarasi di awal dan gak bisa diubah
# harus pake typing.Final, import dulu

from typing import Final

PI: Final = 3.14
print("pi: %F" % (PI))