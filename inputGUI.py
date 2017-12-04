'''
Created on Nov 26, 2017

@author: Romain
'''
from tkinter import *
import GUI
import FileFunction
class inputGUI(object):
    '''
    Create GUI that will display contents of text file / Save contents
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    #Create GUI that will take input.
    def createTextAreaGUI(self, contents, givenFilePath):
        G = GUI.Interface
        FF = FileFunction.FileFunction
        area = Tk()
        area.title("New Files")
        t = Text(area, height=20, width=60)
        t.grid(row = 0, column = 0, columnspan = 3)
        if contents is not None:
            t.insert(END, contents)
        
        def exitWindow():
            area.destroy()
            G.createGUI(0)
            
        def saveTextFile():
            contents = t.get("1.0",END)
            filePath = givenFilePath
            if contents is None:
                messagebox.showwarning("Error", "Cannot save nothing")
                return
            if filePath is not None:
                FF.saveText(0, filePath, contents)
            else:
                filePath = FF.createText(0, contents)
                return filePath
        
        B = Button(area, text = "Save", command = saveTextFile, height=2, width=10, padx=2)
        Q = Button(area, text = "Quit", command = exitWindow, height=2, width=10, padx=2)

        B.grid(row=2, column = 2, padx=(10, 10))
        Q.grid(row=2, column = 0, padx=(10, 10))