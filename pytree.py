from os import listdir
from os.path import abspath, basename, isdir, isfile
from sys import argv

def tree(path, tab):
    print('\n'+tab+basename(path) + '-|')
    tab += '  '
    files = dirs = []

    try:
        dirs = [item for item in listdir(path) if isdir(path+'\\'+item)]
        files = [item for item in listdir(path) if isfile(path+'\\'+item)]
    except:
        pass


    for file in files:
        # first print all files then go to directories
        print(tab+'-'+file)

    for dir in dirs:
        tree(path+'\\'+dir, tab)


def main():
    if not len(argv) > 1:
        return

    path = abspath(argv[1])

    if isdir(path):
        tree(path, '')
    else:
        print("Wrong Input..")
        return

    print('\n')


if __name__ == '__main__':
    main()