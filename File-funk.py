#!/usr/bin/python3

def ffile(path,access,data):


    if access == 'r':
        opfile = open(path,access)
        readf = opfile.readline()
        print(readf)
        opfile.close()
        exit()

    elif access == 'w':
        opfile = open(path,access)
        opfile.write(data)
        opfile.close()
        exit()
    else:
        exit()


ipath = input('Enter path: ')
iaccess = input('Enter access: ')
if iaccess == 'r':
    idata = ''
    ffile(ipath,iaccess,idata)
elif iaccess == 'w':
    idata = input('Enter text:')
    ffile(ipath,iaccess,idata)
else:
    exit()





