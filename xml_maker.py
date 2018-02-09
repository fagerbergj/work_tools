#
#@autor: Jason Fagerberg
#@date: January 29 2018
#@params: txt file with all passes
#@output: xml file for test link
#@assumptions: Only passes are imported, 
#              Testcase abbreviation is on test link circa 1/31
#

from tkinter import *   ## notice lowercase 't' in tkinter here	
from tkinter import filedialog
import os
import time

file_name = ""

#get text box info
def retrieve_input():
	abbr = ["MNP","SSR","ME-8","EZ","MH1","LF","MiHost","CA","OAMP","Geo",
	"ILD","mRDM","Pro","KP","Trans","Hardware","Firmware"]
	input = textBox.get("1.0",END) 
	user = testerBox.get()
	for a in abbr:
		if a in input:
			parse(input,a,user)

#enable tab to next box
def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")
	
def parse(s, t, u):
    while t in s:
        #find MNP
        i = s.find(t)
        #cut all before MNP
        s = s[i:]
        #partician at :
        m = s.partition(":")[0]
        #write to xml
        xml.write("\n\t<testcase external_id=" + '"' + m + '" >\n\t<tester>' + u + "</tester>\n\t<result>p</result>\n\t</testcase>")
        #cut previous MNP
        s = s[4:]
    xml.write("\n</results>")
    xml.close()
    print("XML CREATED AT: " + file_name)
    quit()

root = Tk()
root.withdraw()

#get xml file path
currdir = os.getcwd()
tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select where to save xml')
if len(tempdir) > 0:
	print ("You chose %s" % tempdir)

#build file name
timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = tempdir + "/testlink_" + timestr + ".xml"
print(file_name)

#build file
xml = open(file_name,"a+")

#add header
header = "<?xml version =" + '"' + "1.0" + '" ' + "encoding =" + '"' + "UTF-8" + '"' + "?>\n<results>"
xml.write(header)

root = Tk()
root.title('Passes: ')

#tester
frame = Frame(root, width=500, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=2, relief=RIDGE)
Label(iframe2, text='Tester Name:').pack(side=LEFT,padx=5)
t = StringVar()
testerBox=Entry(iframe2, textvariable=t, bg='white')
testerBox.pack(side=RIGHT,padx=5)
t.set('jfagerberg')
iframe2.pack(expand=1, pady=10, padx=5)

#List of passes
textBox=Text(root, height=50, width=100)
textBox.pack()
buttonCommit=Button(root, height=2, width=20, text="Convert to XML", command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

root.mainloop()