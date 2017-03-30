import hashlib
import os

def hashf1(stroka, sposob):
    stroka = bytes(stroka, encoding='utf8')
    h = hashlib.new(sposob, stroka)
    return h.hexdigest()

fl1 = '/home/ft/Python_lessons_basic/GB_Python2/lesson_1/homework/need_hashes.csv'
fl2 = '/home/ft/Python_lessons_basic/GB_Python2/lesson_1/homework/hashestemp.csv'
f = open(fl1, 'r', encoding='utf-8')
tempf = open(fl2, 'w')
a = ';'
for x in f:
    s = x.split(a)
    shifr = hashf1(s[0], s[1])
    newx = s[0] + a + s[1] + a + shifr + '\n'
    tempf.write(newx)
f.close()
tempf.close()
os.remove(fl1)
os.rename(fl2, fl1)


def test_hashf1_empty_stroka():
    assert hashf1('', 'md5') == 'd41d8cd98f00b204e9800998ecf8427e', 'Неработает хэш'

