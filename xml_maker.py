#
#@autor: Jason Fagerberg
#@date: January 29 2018
#@params: txt file with all passes
#@output: xml file for test link
#@assumptions: Only passes are imported, 
#              Testcase abbreviation is on test link circa 1/31
#

from tkinter import * 
from tkinter import filedialog
import tkinter.messagebox
import os
import time

class XmlMaker():
    def __init__(self):
        #Main window + sizing + position
        self.root = Tk()
        self.root.title('Passes: ')
        w=820
        h=900
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #making frame w/ testername
        self.frame = Frame(self.root, width=500, height=400, bd=1)
        self.frame.pack()
        self.iframe2 = Frame(self.frame, bd=2, relief=RIDGE)
        Label(self.iframe2, text='Tester Name:').pack(side=LEFT,padx=5)
        self.testerBox=Entry(self.iframe2, bg='white')
        self.testerBox.pack(side=RIGHT,padx=5)
        self.testerBox.focus()
        self.iframe2.pack(expand=1, pady=10, padx=5)

        #List of passes
        self.textBox=Text(self.root, height=50, width=100)
        self.textBox.pack()
        self.buttonCommit=Button(self.root, height=2, width=20, text="Convert to XML", command=lambda: self.retrieve_input())
        self.buttonCommit.pack()
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.attributes('-topmost', False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    #get text box info
    def retrieve_input(self):
        if not self.testerBox.get():
            tkinter.messagebox.showinfo("Tester Name Error", "Please Enter Tester Name")
            raise ValueError("Please Enter Tester Name")
        dir = Tk()
        dir.withdraw()

        #get xml file path
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(parent=dir, initialdir=currdir, title='Please select where to save xml')
        if not tempdir:
            return
        if len(tempdir) > 0:
            print ("You chose %s" % tempdir)

        #build file name
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.file_name = tempdir + "/testlink_" + timestr + ".xml"
        print(self.file_name)

        #build file
        self.xml = open(self.file_name,"a+")

        #add header
        header = "<?xml version =" + '"' + "1.0" + '" ' + "encoding =" + '"' + "UTF-8" + '"' + "?>\n<results>"
        self.xml.write(header)
        abbr = ["MNP","SSR","ME-8","EZ","MH1","LF","MiHost","CA","OAMP","Geo","ILD","mRDM","Pro","KP","Trans","Hardware","Firmware"]
        test_results = self.textBox.get("1.0",END) 
        user = self.testerBox.get()
        for a in abbr:
            if a in test_results:
                self.parse(test_results,a,user)

    #enable tab to next box
    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return("break")
    
    def on_closing(self):
        self.root.quit()
        
    def parse(self, s, t, u):
        while t in s:
            #find MNP
            i = s.find(t)
            #cut all before MNP
            s = s[i:]
            #partician at :
            m = s.partition(":")[0]
            #write to xml
            self.xml.write("\n\t<testcase external_id=" + '"' + m + '" >\n\t<tester>' + u + "</tester>\n\t<result>p</result>\n\t</testcase>")
            #cut previous MNP
            s = s[4:]
        self.xml.write("\n</results>")
        self.xml.close()
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, "XML CREATED AT: " + self.file_name)

XmlMaker()