'''
Created on Sep 29, 2013

@author: Strahinja
'''

import os
from os.path import isdir, isfile, join

def printDir(path, depth):
    directories = []
    files = []
    for child in os.listdir(path):
        if isdir(join(path,child)):
            directories.append(child)
        elif isfile(join(path,child)):
            files.append(child)
    directories.sort(key=None, reverse=False)
    files.sort(key=None, reverse=False)
    
    for directory in directories:
        print("\t"*depth + "[" + directory + "]")
        printDir(join(path,directory), depth+1)
    for file in files:
        print("\t"*depth + file)
    
    
    
printDir("..", 0)