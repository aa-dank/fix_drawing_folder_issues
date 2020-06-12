import os, csv, shutil, errno, json, glob
'''Searches for drawings folders that do not have an F5 - Drawings folder and nests its content in
a newly created F5 - drawings folder. Records what it does to csv file'''



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

##################################################################################################

jsonLog = "F5_drawing_log.json"
log = []
changeDict = {'errors':{}, 'changes':{}}

d = '.'
#k = [os.path.join(d, o) for o in os.listdir(d)
#                    if os.path.isdir(os.path.join(d,o))]


dir  = input("Enter filepath to record server parent directory: ")
if dir == "test":
    dir = "S:\Project Folders\Aaron Dankert\Test2"

for root, dirs, files in os.walk(dir):

    rootList = splitall(root)
    hasF5Folder = False



    if 'F - ' in rootList[-1]:
        for folder in dirs:
            if 'F5' in folder:
                hasF5Folder =True

        if not hasF5Folder:
            #import pdb; pdb.set_trace()
            dest = "F5 - Drawings and Specifications"
            changeDict['changes'][root] = {}
            changeDict['changes'][root]['preRoot'] = root[:-len(rootList[-1])]
            changeDict['changes'][root]['newF5'] = os.path.join(root, "F5 - Drawings and Specifications")
            changeDict['changes'][root]['old Fold'] = rootList[-1] #will be old folder name




for dir, renameParts in changeDict['changes'].items():
    f5Name = "F5 - Drawings and Specifications"
    #import pdb; pdb.set_trace()
    preRoot = changeDict['changes'][dir]['preRoot']
    oldFold = changeDict['changes'][dir]['old Fold']
    os.chdir(preRoot)
    hasParallelF5 = False


    for item in os.listdir(preRoot): #check if there is a paralell F5 folder in path
        if item.startswith('F5') or item.startswith('f5'):
            changeDict['errors'][dir] = {}
            changeDict['errors'][dir]['error'] = "Has a Parallel 'F5' folder."
            changeDict['errors'][dir]['preRoot'] = preRoot
            hasParallelF5 = True


    if not hasParallelF5:
        try:
            #import pdb; pdb.set_trace()
            os.rename(oldFold, f5Name)
            os.mkdir(oldFold)
            shutil.move(f5Name, oldFold)
            changeDict['changes'][root]['success'] = 'yes'
            print("New Change: " + preRoot + f5Name)

        except Exception as e::
            #import pdb; pdb.set_trace()
            changeDict['errors'][dir] = {}
            changeDict['errors'][dir]['error'] = str(e)
            changeDict['errors'][dir]['preRoot'] = preRoot
            print("error with rename in %s" % (dir))

    #newFPath = os.path.join(preRoot, "F - Drawings and Specifications")

import pdb; pdb.set_trace()

with open(jsonLog, 'w') as addDataFile:
    json.dump(changeDict, addDataFile)
