import os, csv, shutil, errno, json, glob

testMaterialLoc = r'S:\Project Folders\Aaron Dankert\TEST FILES'
testLoc = r"S:\Project Folders\Aaron Dankert\Test2"


def empty_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
                return(e)

firstError = empty_folder(testLoc)
if firstError:
    print("If error, this is it: " + firstError)

for item in os.listdir(testMaterialLoc):
    try:
        import pdb; pdb.set_trace()
        itemPath = os.path.join(testMaterialLoc, item)
        shutil.copy(itemPath, testLoc)
    except Exception as z:
        print("Error: " + item)
