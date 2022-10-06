from os import listdir
from os.path import abspath, basename, isdir, isfile, sep
from sys import argv
import argparse


def tree(path, tab):
    print('\n'+tab+basename(path) + '-|')
    tab += '  '
    files = dirs = []

    try:
        dirs = [item for item in listdir(path) if isdir(path+sep+item)]
        files = [item for item in listdir(path) if isfile(path+sep+item)]
    except:
        pass


    for file in files:
        # first print all files then go to directories
        print(tab+'-'+file)

    for dir in dirs:
        tree(path+'\\'+dir, tab)


def main(path):

    if isdir(path):
        tree(path, '')
    else:
        print("Wrong Input..")
        return

    print('\n')


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="pytree")
	parser.add_argument("path", help="Path of request directory")

	args = parser.parse_args()

	main(args.path)
