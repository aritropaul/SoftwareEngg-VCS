import os
import shutil
from distutils.dir_util import copy_tree


masterRepo = raw_input("Enter Repository Name: ")


#set up master
masterBranch = masterRepo+"/masterBranch/"
directory = os.path.dirname(masterBranch)
if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


#create new branches
def branch(newBranch):

    newBranch = masterRepo+"/"+newBranch+"/"
    directory = os.path.dirname(newBranch)
    os.makedirs(directory)

def setUp():
        SRS = masterBranch + "SRS/"
        dirSRS = os.path.dirname(SRS)
        os.makedirs(dirSRS)
        SDS = masterBranch + "SDS/"
        dirSDS = os.path.dirname(SDS)
        os.makedirs(dirSDS)
        Test = masterBranch + "Test/"
        dirTest = os.path.dirname(Test)
        os.makedirs(dirTest)

#local repo
def init():
    localRepo = masterRepo+"/localRepo/"
    directory = os.path.dirname(localRepo)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    setUp()
    return localRepo
    


#add/commit files
def commit(fileDirectory):
    maindir = masterRepo+"/localRepo/"
    copy_tree(fileDirectory, maindir+"rev/")

def push(thisbranch = masterBranch):
    branchLoc = thisbranch+"/"
    maindir = masterRepo+"/localRepo/"
    copy_tree(maindir+"rev/", branchLoc)
    check()


def check():
    check = [1,1,1]
    if not os.listdir(masterBranch+"SRS/"):
        print('SRS Remaining')
    else:
        check[0] = 0
    if not os.listdir(masterBranch+"SDS/"):
        print('SDS Remaining')
    else:
        check[1] = 0
    if not os.listdir(masterBranch+"Test/"):
        print('Test Report Remaining')
    else:
        check[2] = 0
    if(check == [0,0,0]):
        print('Everything Done.')


def commandLine():
   cmd = " "
   while(cmd != "exit" or cmd != "EXIT"):
       cmd = raw_input(" > ") 
       if(cmd == "soft init"):
           maindir = init()
       if(cmd == "soft commit"):
           commit("/Users/aritropaul/Documents/Winter Sem 2017-18/Software/Project/PySoft/Fol 1/")
       if(cmd == "soft push"):
            branchName = raw_input("> Branch : ")
            if(branchName == "master"):
                push(masterBranch)
            else:
                push(branchName)

commandLine()