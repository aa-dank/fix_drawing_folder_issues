import os, datetime, re, shutil, csv
import pandas as pd
from pprint import pprint

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

def user_chooses_yes_no(promptText):
    '''asks yes or no question to user and returns 'True' for a yes answer and 'False' for a no answer'''
    yesNo = ['yes', 'y', 'Yes', 'Y', 'No', 'no', 'n', 'N']
    response = ''
    while response not in yesNo:
        response = input(promptText)
    if response in yesNo[4:]:
        return False
    else:
        return True

def exit_program():
    '''Exits from the program'''
    print("Exiting Program")

def user_csv_choice():
    '''Prompts user for csv file and checks that the user string corresponds to a file in current directory'''
    aPrompt = "Enter csv filename including its extension." + os.linesep + "(The file must be in same directory as this script.)"
    userStr = input(aPrompt)
    try:
        os.path.isfile(os.path.join(os.getcwd(), userStr))
    except:
        print("error occured with that filename. Try again.")
        user_csv_choice()

    return userStr

def tsv_to_csv(tsv, csv):
    '''Creates csv file from tab delimited file, tsv'''
    df = pd.read_csv(tsv, sep= '\t')
    df.to_csv(csv, index=False)


def deaggregate_f_folder(aDirObj):
    '''For a given directory this function moves directories with "F<Number>" at  begining of name outside the given Directory and
    renames the given directory to 'F5 - Drawings and Specifications' '''
    f5FolderName = "F5 - Drawings and Specifications"
    os.chdir(aDirObj.preRoot)
    for aDir in os.listdir(aDirObj.path):
        if re.match('^[Ff][0-9]', aDir):
            aDir_OldPath = str(os.path.join(aDirObj.path, aDir))
            try:
                shutil.move(aDir_OldPath, aDirObj.preRoot)
            except:
                return False

    # rename directory from "F - " to "F5"
    newName = str(os.path.join(aDirObj.preRoot, f5FolderName))
    try:
        os.rename(aDirObj.path, newName)
        return True
    except:
        return False



def f_to_f5(someDirObj):
    '''Rename the directory to 'F5 - Drawings and Specifications'.'''

    f5FolderName = "F5 - Drawings and Specifications"
    os.chdir(someDirObj.preRoot)
    newName = str(os.path.join(someDirObj.preRoot, f5FolderName))
    try:
        os.rename(someDirObj.path, newName)
        return True
    except:
        return False

def mark_for_later():
    '''Mark for later processing if the issue cannot be fixed with this script'''
    return True

def user_chooses_action(funcList):

    '''1. Turns list of function dictionaries into choice tree from which user can select an option.
            Dictionary must look like {'name': <function name>, 'desc':<description for user>, 'args': <List of Arguments>}
            (Note: args need to be in order)
            if the function has an empty 'desc' attribute, it will take the description from the function declaration
        2. Prompts user to select a command choice
        3. returns funcList dictionary with a result key for everyfunction that was run.'''
    funError = False
    for fun in funcList:
        if callable(fun['function']):
            fun['name'] = fun['function'].__name__
            if fun['desc'] == '':
                fun['desc'] = fun['function'].__doc__
        else:
            fun['error'] = 'Error raised when checking if a function was callable'
            funError = True
    # report anything passed to funcList argument that is not an argument
    if funError:
        funIssuesMessage = "There was an issue with at least one of the functions. \nThe functions successfully parsed are: "
        for fun2 in funcList:
            if 'error' not in list(fun2.keys()):
                funIssuesMessage += os.linesep + fun2['name']
        print(funIssuesMessage + os.linesep + "Script Stopped")
        exit()
    else:
        # Following code creates a prompt describing the options available to the user
        prompt = "Choose from the following options:"
        optionNums = list(map(str, list(range(1, len(funcList) + 1))))  # create list of string number commands
        tab = "    "
        i = 0
        for fun3 in funcList:
            choice = str(1 + i)
            i += 1
            fun3['choice number'] = choice
            prompt += os.linesep + tab + choice + " -- " + fun3['name']
            prompt += os.linesep + tab + tab + "Description:  " + fun3['desc']
        prompt += os.linesep + "Enter command choice:"

        userCommand = ''
        while userCommand not in optionNums:  # prompt user for function to use
            userCommand = input(prompt)
            if userCommand not in optionNums:
                print("Not a valid choice.")

        for fun4 in funcList:
            #import pdb;pdb.set_trace()
            if fun4["choice number"] == userCommand:
                try:
                    argList = fun4['args']
                    fun4['results'] = fun4['function'](*argList)
                except:
                    print("There was an issue running function, " + fun4['name'] + os.linesep + "Ending Script")
                    exit()
    return funcList

def process_path_f5_issues(issuesDF):
    '''Function specific to this script that iterates over the dataframe, asking the user how to process each
    database issue and executes the command. Reliees on user_chooses_action function.'''

    date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    nos = ["No", "no", "n"]
    for index, row in issuesDF.iterrows():
        #import pdb;pdb.set_trace()
        if row['Fixed'] in nos and row['Needs_Attention'] in nos:
            directoryToFix = directory_obj(row['path'])
            directoryToFix.add_dir_trees_attr() #add directory tree dictionary to attributes
            directoryToFix.add_file_trees_attr()
            #import pdb;pdb.set_trace()

            commandsList = [{'function': directoryToFix.see_tree,
                         'desc': "Print the directory tree *with files* from selected directory",
                         'args': [directoryToFix.parent_files]},
                        {'function': directoryToFix.see_tree,
                         'desc': "Print directory tree from filepath selected directory",
                         'args': [directoryToFix.parent_tree]},
                        {'function': f_to_f5, 'desc': '', 'args': [directoryToFix]},
                        {'function': deaggregate_f_folder, 'desc': '', 'args': [directoryToFix]},
                        {'function': mark_for_later, 'desc': '', 'args': []},
                        {'function': exit_program, 'desc': '', 'args': []}]

            print(os.linesep + os.linesep + "Directory:  " + directoryToFix.path)
            commandsList = user_chooses_action(commandsList)
            #import pdb;pdb.set_trace()
            #depending on which function is run, an indicator is included in the dataframe.
            if 'f_to_f5' == [x for x in commandsList if 'results' in x.keys()][0]['name']:
                issuesDF.at[index, 'Fixed'] = date
                break
            if 'mark_for_later' == [x for x in commandsList if 'results' in x.keys()][0]['name']:
                #import pdb;pdb.set_trace()
                issuesDF.at[index, 'Needs_Attention'] = date
                break
            if 'deaggregate_f_folder' == [x for x in commandsList if 'results' in x.keys()][0]['name']:
                #import pdb; pdb.set_trace()
                issuesDF.at[index, 'Fixed'] = date
                break
            if 'exit_program' == [x for x in commandsList if 'results' in x.keys()][0]['name']:
                return issuesDF

            process_path_f5_issues(issuesDF)
    return issuesDF

class directory_obj:
    def __init__(self, folderPath):
        self.path = folderPath

        self.rootList = splitall(folderPath) #folder path as list
        self.preRoot = folderPath[:-len(self.rootList[-1])]

    def see_tree(self, treeDict = None, indent = 4):
        '''pretty prints the dictionary representation of the directory tree, treeDict'''
        if treeDict == None and hasattr(self, 'my_tree'):
            treeDict = self.my_tree
        print(os.linesep + os.linesep + "Folder Structure:")
        pprint(treeDict)

    def f5_test(self, checkDir = None, selectedRoot = None):
        '''checks to see if checkDir file path has an 'F - Drawings' folder
            but no 'F5 - Drawings' folder'''
        resultDict = {}
        if checkDir == None:
            checkDir = self.path

        for root, dirs, files in os.walk(checkDir):
            #issues[0] designates whether there is a drawing folder but no F5 folder
            #issues[1] designates whether there is a parallel F5 folder
            issues = ["No", "No"]
            rootList = splitall(root)
            #import pdb; pdb.set_trace()
            if 'F - ' in rootList[-1]:
                for folder in dirs:
                    if 'F5' in folder:
                        issues[0] = "No"
                        break
                    else:
                        issues[0] = "Yes"
                #puts path to root selected directory in selectedRoot variable.(Note: This is ugly and there is a better way to do this with unipath library)
                selectedRoot = root[:-len(splitall(root)[-1])][:-1]

                for item in os.listdir(selectedRoot):  # check if there is a paralell F5 folder in path
                    if item.startswith('F5') or item.startswith('f5'):
                        #import pdb; pdb.set_trace()
                        issues = ["No", "Yes"]

            if "Yes" in issues:
                resultDict[root] = issues
        return resultDict

    def apply_tests(self, funcList):
        '''returns dictionary of function name keyed to output'''
        results = {}
        for func in funcList:
            if callable(func):
                results[func.__name__] = func(self.path)

            else:
                print("one of the test functions appears to not actually be a function.")
        return results

    def fs_tree_to_dict(self, path_ = None, filesToo=False):
        '''creates dictionary that parallels the structure of directories in path.
            If filesToo, the function includes files in the dictionary.
            This was adapted from here: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python'''
        if path_ == None:
            path_ = self.preRoot

        file_token = ''
        for root, dirs, files in os.walk(path_):
            tree = {d: self.fs_tree_to_dict(os.path.join(root, d), filesToo) for d in dirs}
            if filesToo:
                tree.update({f: file_token for f in files})
            #if path_ == self.preRoot:
            #   self.dirTree = tree
            #if path_ != self.preRoot:
            return tree

    def add_dir_trees_attr(self):
        self.my_tree = self.fs_tree_to_dict(self.path)
        self.parent_tree = self.fs_tree_to_dict()

    def add_file_trees_attr(self):
        self.my_files = self.fs_tree_to_dict(self.path, filesToo=True)
        self.parent_files = self.fs_tree_to_dict(filesToo=True)



if __name__ == '__main__':
    tsvFile = "Drawing_Dir_No_F5.tsv"
    tsvPath = os.path.join(os.getcwd(), tsvFile)
    csvFile = "Drawing_Dir_No_F5.csv"
    command = ''
    commandChoices = ['1', '2']
    while command not in commandChoices:
        command = input("Enter '1' to start search for issues." + os.linesep + "Enter '2' to start correcting issues from csv." + os.linesep + "Enter command number: ")

    #if user wants to hunt for issues
    if command == '1':
        selectedDir = ''
        while not os.path.isdir(selectedDir):
            selectedDir = input("Enter directory from where search will start:  ")
            if selectedDir == 'td':
                selectedDir = r"C:\Users\adankert\Desktop\TestDesk"

        selectedDir = os.path.normpath(selectedDir)

        fileIssues = []
        issuesDict = {}
        issueNum = 0 #tracks number of problems found
        selected = directory_obj(selectedDir)
        test = selected.f5_test

        selectedIssues = selected.apply_tests([test]) #dictionary of function name keyed to list of two boolean values
        #import pdb;pdb.set_trace()

        if selectedIssues[test.__name__]:
            for pth, listOfIssues in selectedIssues[test.__name__].items():
                issueNum += 1
                if (issueNum % 3) == 0:  # print running tally of issues found
                    print("Total number of issues found thus far: " + str(issueNum))
                fileIssues.append([pth, selectedIssues[test.__name__][pth][0], selectedIssues[test.__name__][pth][1], "No", "No", "No"])

        #append the list of fileIssues to the csv file by using dataframes
        #import pdb; pdb.set_trace()
        DF = pd.read_csv(tsvPath, sep = '\t')
        newIssuesDF = pd.DataFrame(fileIssues, columns=["path", "Drawing_but_no_F5", "Paralell_F5", "Fixed", "Needs_Attention", "Errors"])
        DF = DF.append(newIssuesDF)
        DF.drop_duplicates(subset="path", keep='first', inplace=True) #eliminates rows if they have same path as previous entry in csv file


        DF.to_csv(tsvPath, index=False, sep= '\t')
        tsv_to_csv(tsvFile,csvFile)

        print("Issues saved to following file: " + csvFile)
        '''Getting multiple entries for each folder issue. Need to reduce to a single os.walk function.'''

    #if user shooses to start correcting issues
    if command == '2':
        csvPrompt = "Use %s as list of issues?" % tsvFile
        if not user_chooses_yes_no(csvPrompt):
            tsvFile = user_csv_choice()
            tsvPath = os.path.join(os.getcwd(), tsvFile)

        problemsDF = pd.read_csv(tsvPath, sep= '\t')
        #import pdb; pdb.set_trace()

        problemsDF.Fixed = problemsDF.Fixed.astype(str, copy=False)
        problemsDF.Needs_Attention = problemsDF.Needs_Attention.astype(str, copy=False)

        problemsDF = process_path_f5_issues(problemsDF)
        '''Next: iterate over DF and ask user how to deal with each issue. Execute desired functions.
        Also deal with f_but_no_f5 function.'''
        #import pdb; pdb.set_trace()
        problemsDF.to_csv(tsvPath, index=False, sep= '\t')
        tsv_to_csv(tsvFile, csvFile)
