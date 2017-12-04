'''
Created on Nov 26, 2017

@author: Romain
'''

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
class FileFunction(object):
    '''
    Class that handles any reading or writing for text files / Dat file
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    #Open text file
    def openTextFile(self, filePath):
        if filePath is None:
            Tk().withdraw()
            filePath = askopenfilename()
            if filePath is None:
                return None
            f = open(filePath, 'r')
            contents = f.read()
            f.close()
            FileFunction.writeToDatFile(0, filePath, os.path.basename(filePath))
            return contents, filePath
        else:
            f = open(filePath, 'r')
            contents = f.read()
            f.close()
            FileFunction.writeToDatFile(0, filePath, os.path.basename(filePath))
            return contents
    
    #Create text file.
    def createText(self, contents):
        Tk().withdraw()
        filePath = asksaveasfilename(defaultextension=".txt")
        if filePath is None:
            return None
        f = open(filePath, 'w')
        f.write(contents)
        f.close()
        return filePath
    
    #Save text file.
    def saveText(self, filePath, contents):
        f = open(filePath, 'w')
        f.write(contents)
        f.close()
    
    #Create dat file.
    def createDatFile(self):
        f = open('list.dat', 'a')
        f.close()
    
    #Check to see if Dat file exists, If it doesn't then create it.
    def DatFileExists(self):
        path = os.path.dirname(os.path.realpath(__file__))
        if os.path.exists(path + "/list.dat"):
            return True
        else:
            return False
    
    #Read the Dat file and return a list of text files in Dat file.
    def getFileList(self):
        results = []
        datFile = os.path.dirname(os.path.realpath(__file__)) + "/list.dat"
        f = open(datFile, 'r')
        for line in f:
            fields = line.split('|')
            results.append(fields[2])
        f.close()
        return results
    
    #Open text file and return the contents
    def getFileContents(self, index):
        datFile = os.path.dirname(os.path.realpath(__file__)) + "/list.dat"
        f = open(datFile, 'r')
        for line in f:
            fields = line.split('|')
            if int(fields[0]) == index:
                filePath = fields[1]
        return FileFunction.openTextFile(0, filePath)
        f.close()
    
    #Check to see if file exists within the Dat file and if it does return the index and line from Dat file.
    def fileExists(self, filePath):
        datFile = os.path.dirname(os.path.realpath(__file__)) + "/list.dat"
        f = open(datFile, 'r')
        index = 1
        for line in f:
            fields = line.split('|')
            if fields[1] == filePath:
                return index,line
            else:
                index = index + 1
        return None,None
        f.close()
    
    #Read Dat file and return the results.
    def readDatFile(self):
        results = []
        datFile = os.path.dirname(os.path.realpath(__file__)) + "/list.dat"
        f = open(datFile, 'r')
        for line in f:
            fields = line.split('|')
            results.append(fields[0] + "|" +  fields[1] + "|" + fields[2])
        f.close()
        return results
    
    #Write information to Dat file.
    def writeToDatFile(self, filePath, textFile):
        datFile = os.path.dirname(os.path.realpath(__file__)) + "/list.dat"
        results = FileFunction.readDatFile(0)
        index,testing = FileFunction.fileExists(0, filePath)
        newInfo = "1|" + filePath + "|"  + textFile + "\n"
        if index is None:
            index = 1
            f = open(datFile, 'w')
            f.write(newInfo)
            f = open(datFile, 'a')
            for line in results:
                fields = line.split('|')
                if int(fields[0]) >= index:
                    fields[0] = str(int(fields[0]) + 1)
                    f.write(str(fields[0] + "|" + fields[1] + "|" + fields[2]))
            f.close()
            return
        elif index == 1:
            return
        else:
            f = open(datFile, 'w')
            f.write(newInfo)
            f = open(datFile, 'a')
            for line in results:
                fields = line.split('|')
                if int(fields[0]) == index:
                    results.remove(testing)
            for line in results:
                fields = line.split('|')
                if int(fields[0]) < index:
                    fields[0] = str(int(fields[0]) + 1)
                    f.write(str(fields[0] + "|" + fields[1] + "|" + fields[2]))
                else:
                    f.write(str(fields[0] + "|" + fields[1] + "|" + fields[2]))
            f.close()
            return