import os

def list_files(startpath):

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


if __name__ == '__main__':
    dir = input("Enter filepath to record server parent directory: ")
    if dir == "test":
        dir = "S:\Project Folders\Aaron Dankert\Test2"
    dir = os.path.normpath(dir)
    list_files(dir)