import hashlib
import os

dirf = '/home/ft/Python_lessons_basic/GB_Python2/lesson_1/homework/files/file2/'
mdf = 'parts.md5'


def shrink(f, by):
    '''

    Разбиение  на части

    '''
    os.chdir(os.path.dirname(f))
    n = 1
    if os.access(f, os.F_OK):
        fi = open(f, 'rb')
        st = bytearray(fi.read())
        by = int(by)
        while len(st) > by:
            part = st[:by]
            del st[:by]
            k = open(str(n), 'wb')
            k.write(part)
            k.close()
            n += 1
        k = open(str(n), 'wb')
        k.write(st)
        k.close()
    return n


def xmd(dirf, outf):
    '''

       Создание файла с хэшами

    '''
    os.chdir(dirf)
    k = open(outf, 'w')
    s = os.listdir(dirf)
    n = 0
    for x in s:
        if os.path.isfile(x):
            if x != outf:
                f = open(x, 'rb')
                st = f.read()
                f.close()
                h = hashlib.new('md5', st)
                k.write(h.hexdigest() + '\n')
                n += 1
    k.close()
    return n


def concat(dirf, mdf, outf):
    '''

           Собираем кусочки пазла

    '''
    os.chdir(dirf)
    if os.access(mdf, os.F_OK):
        hashf = open(mdf, 'r')
        hsp = []
        for x in hashf:
            hsp.append(x.rstrip("\n"))
        rightsp = list('' for x in hsp)
        hashf.close()
    else:
        return 'Нет доступа к файлу хеша'
    s = os.listdir(dirf)
    for x in s:
        if os.path.isfile(x):
            if x != mdf:
                f = open(x, 'rb')
                st = f.read()
                f.close()
                h = hashlib.new('md5', st)
                rightsp[hsp.index(h.hexdigest())] = st
    r = b''.join(rightsp)
    ff = open(outf, 'wb')
    ff.write(r)
    ff.close()
    os.path.getsize(outf)
    return os.path.getsize(outf)







#print(concat(dirf, mdf, 'out1'))
#print(shrink('/home/ft/Python_lessons_basic/GB_Python2/lesson_1/README.MD', 15))
#print(xmd('/home/ft/Python_lessons_basic/GB_Python2/lesson_1/homework/files/file1/', '10101'))
