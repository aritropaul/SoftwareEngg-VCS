import os
import shutil
from distutils.dir_util import copy_tree
import cPickle as pickle

class sftobject:
    fileDir = ""
    revisionNumber = 0

localObject = sftobject()


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
    ###
    # revisionFile = maindir+"rev/"+"Revision.sft"
    # fi = open(revisionFile,"w+")
    # pickle.dump(localObject,fi)
    # fi.close()
    # ###
    fileLocation = fileDirectory
    # ###
    # fo = open(revisionFile,"rb")
    # Obj = pickle.load(fo)
    # localObject.revisionNumber = Obj.revisionNumber + 1
    # fo.close()
    # localObject.fileDir = fileLocation
    # ###
    # fi = open(revisionFile,"wb")
    # pickle.dump(localObject,fi)
    # fi.close()
    ###
    copy_tree(fileLocation, maindir+"rev/")
    # Obj = pickle.load(fi)
    # print(localObject.fileDir)
    # print(localObject.revisionNumber)


maindir = init()
commit("/Users/aritropaul/Documents/Winter Sem 2017-18/Software/Project/PySoft/Fol 1/")