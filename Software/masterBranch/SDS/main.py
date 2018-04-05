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
    return localRepo


#add/commit files
def commit(fileDirectory):
    fileLocation = fileDirectory
    copy_tree(fileLocation, maindir+"rev/")


maindir = init()
commit("/Users/aritropaul/Documents/Winter Sem 2017-18/Software/Project/PySoft/Fol 1/")
setUp()
if not os.listdir(masterBranch+"SRS/"):
    print('SRS Remaining')
if not os.listdir(masterBranch+"SDS/"):
    print('SDS Remaining')
if not os.listdir(masterBranch+"Test/"):
    print('Test Remaining')