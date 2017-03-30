import random
import string


def create_file(namef, dirf, size):
        def randomj(size2):
            r = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(size2))
            return r

        if not size.isdigit():
                if size.endswith('KB'):
                        s1 = size.split('KB')
                        size1 = int(s1[0]) * 1024
                elif size.endswith('MB'):
                        s1 = size.split('MB')
                        size1 = int(s1[0]) * 1048567
                elif size.endswith('GB'):
                        s1 = size.split('GB')
                        size1 = int(s1[0]) * 1073741824
                else:
                        assert size[-1] == 'B', 'Неожиданное значение'
                        size1 = int(size[:-1])

        else:
                size1 = int(size)

        token = randomj(size1)
        file = open(dirf + namef, "w")
        file.write(token)
        file.close()


create_file("/test1.txt", "/home/ft", '10KB')
create_file("/test2.txt", "/home/ft", '1024')
create_file("/test11.txt", "/home/ft", '2MB')
create_file("/test21.txt", "/home/ft/", '1B')
