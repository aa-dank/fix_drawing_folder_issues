import os, csv
'''
From Chosen parent directory, this crawls through folders looking for tiff folders not in a drawing folder
and puts their location in a csv file.
'''



class folder:

    def __init__(name, path):
        self.name = name
        self.path = path
        self.fileExt = file.split('.')[-1]
        
def splitall(path):
    '''splits a path into each piece that corresponds to a mount point, directory name, or file'''
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

dir  = input("Enter filepath to record server parent directory: ")
if dir == "test":
    dir = "S:\Project Folders\Aaron Dankert\TEST FILES"
'''
recipientDir = input("Enter filepath to record server parent directory: ")
if recipientDir == "t":
    recipeintDir = ""
'''
log = {"TIFF folder locations":[]}

for root, dirs, files in os.walk(dir):
    rootList = splitall(root)
    withinDrawings = False
    i = 0
    for folder in rootList:
        if "F5" in folder or "F - " in folder:
            withinDrawings = True
    for folder in rootList:
        ### strip spaces from last directory in path and check if its a tiff folder
        if rootList[-1].strip() in ["TIFF", "Tiff", "tiff", "TIFF"] and not withinDrawings:
                #import pdb; pdb.set_trace()
                #root2 = u"\\\\?\\" + root    ### useful for if the filenames are too long
                newFolderRoot = root[:-2]


                alreadyRecorded = False
                for path in log["TIFF folder locations"]:
                    if path[0] == root:
                        alreadyRecorded = True
                        break

                if not alreadyRecorded:
                    log["TIFF folder locations"].append([root])





with open('Tiff_folders_no_Drawing_folder.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, lineterminator='\n')
    writer.writerows(log["TIFF folder locations"])
