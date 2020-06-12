import os, json, shutil
data = {}
with open('F5_drawing_log.json') as json_file:
    data = json.load(json_file)


for dir, renameParts in data.items():
    #os.rename(dir, renameParts['newF5'])
    preRoot = renameParts['preRoot']
    newFPath = os.path.join(preRoot, "F - Drawings and Specifications")
    try:
        os.mkdir(newFPath)
    except OSError:
        print ("Creation of the directory %s failed" % newFPath)
    try:
        shutil.move(renameparts['newF5'], newFPath)
    except:
        print ("Moving of the directory %s failed" % newFPath)
