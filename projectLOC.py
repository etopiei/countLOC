#Get Lines of Code In Entire Project
#Author: etopiei
#Written 2016
#Usage: python projectLOC.py [directory of project]
#Note: Do NOT use a trailing slash in the directory

import os, sys

class Class1:
    total = 0

allowedExtensions = ['.html','.css','.js','.php','.c','.py']

def iterateThroughFiles(dir,classAccess):

    print("Checking: {}".format(dir))

    if (os.path.isdir(dir)):
    
        for filename in os.listdir(dir):
            name, ext = os.path.splitext(filename)
            if (ext not in allowedExtensions):
                if (os.path.isdir(dir+'/'+filename) and ('.' not in filename)):
                    iterateThroughFiles(dir+'/'+filename,classAccess)
                print("Skipping: {}".format(filename))
            else:
                 print("Counting: {}".format(filename))
                 fullName = dir + '/' + filename
                 x = file_len(fullName)
                 classAccess.total = classAccess.total + x
    
    else:

        return "Error"

    return

def file_len(fname):
    
    with open(fname) as f:
        i = -1
        for i, l in enumerate(f):
            pass
    return i + 1

classAccess = Class1()

loc = iterateThroughFiles(sys.argv[1],classAccess)

if (loc == "Error"):
    print("There was an issue accessing the dircetory. Please try again.")
else:
    print('The total lines of code in your project is...')
    print(classAccess.total)
