'''
Created on Nov 26, 2017

@author: Romain
'''
from tkinter import *
import FileFunction
import inputGUI
import sys
class Interface(object):
    '''
    Main interface for application
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    #Create main GUI
    def createGUI(self):
        GUI = Tk()
        GUI.title("Python Picker")
        ff = FileFunction.FileFunction
        nf = inputGUI
        textFileList = ff.getFileList(0)
        
        if ff.DatFileExists(0) is False:
            ff.createDatFile(0)
        
        def openTextFile():
            contents,givenFilePath = ff.openTextFile(0, None)
            if contents is None:
                messagebox.showerror("Error", "No file selected")
            nf.inputGUI.createTextAreaGUI(0, contents, givenFilePath)
            GUI.destroy()
            
        def exitWindow():
            GUI.destroy()
            sys.exit()
            
        def newTextFile():
            contents = None
            nf.inputGUI.createTextAreaGUI(0, contents, None)
            GUI.destroy()
        
        def onselect(evt):
            # Note here that Tkinter passes an event object to onselect()
            w = evt.widget
            index = int(w.curselection()[0]) + 1
            contents = ff.getFileContents(0,index)
            nf.inputGUI.createTextAreaGUI(0, contents)
            GUI.destroy()
        
        listbox = Listbox(GUI)
        for line in textFileList:
            listbox.insert(END, line)
        listbox.grid(row = 0, column = 3, rowspan = 3, columnspan = 4)
        listbox.bind('<<ListboxSelect>>', onselect)

        B = Button(GUI, text = "Open", command = openTextFile, height=2, width=10, padx=2)
        Q = Button(GUI, text = "Quit", command = exitWindow, height=2, width=10)
        R = Button(GUI, text = "New", command = newTextFile, height=2, width=10)

        B.grid(row=0, column = 0, padx=(10, 10))
        Q.grid(row=2, column = 0, padx=(10, 10))
        R.grid(row=1, column = 0, padx=(10, 10))
        GUI.mainloop()