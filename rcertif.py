from tkinter import *
#from report import report
from analyzer import analyzer

root = Tk()


class MyDialog:
    diffindex = 1
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='Enter your response below')
        self.myLabel.pack()

        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()

        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        global username
        username = self.myEntryBox.get()
        self.top.destroy()



def analyze():
    t3.insert(END, "\nStarted Analyzing ...")    
    result = analyzer.analyzer_getstatus()
    temp = "\nTotal Requirements found " + str(result['totreq'])
    t3.insert(END, temp)
    temp = "\nTest case mapped requirements " + str(result['mapreq'])
    t3.insert(END, temp)
    temp = "\nReq Text Content are same for " + str(result['same'])
    t3.insert(END, temp)
    temp = "\nReq Text Content are changed for " + str(result['suspect'])
    t3.insert(END, temp)
    #print(config_info)


def startdiff():
    tmpstr = "\n\nShowing Diff for 1 Requirement"
    t3.insert(END, tmpstr)
    temp = analyzer.analyzer_getdifftext(MyDialog.diffindex)
    t1.delete(1.0,END)
    t1.insert(END,temp['reqtext'])
    t2.delete(1.0,END)
    t2.insert(END,temp['reptext'])

def previous():

    MyDialog.diffindex = MyDialog.diffindex - 1

    if MyDialog.diffindex > 0:
        tmpstr = "\n\nShowing Diff for " + str(MyDialog.diffindex) + " Requirement"
        t3.insert(END, tmpstr)
        temp = analyzer.analyzer_getdifftext(MyDialog.diffindex)
        t1.delete(1.0,END)
        t1.insert(END,temp['reqtext'])
        t2.delete(1.0,END)
        t2.insert(END,temp['reptext'])
    else:
        tmpstr = "\n\nNo More Difference"
        t3.insert(END, tmpstr)


def next():

    result = analyzer.analyzer_getstatus()
    req_change = result['suspect']

    MyDialog.diffindex = MyDialog.diffindex + 1

    if MyDialog.diffindex <= req_change:
        tmpstr = "\n\nShowing Diff for " + str(MyDialog.diffindex) + " Requirement"
        t3.insert(END, tmpstr)
        temp = analyzer.analyzer_getdifftext(MyDialog.diffindex)
        t1.delete(1.0,END)
        t1.insert(END,temp['reqtext'])
        t2.delete(1.0,END)
        t2.insert(END,temp['reptext'])

    else:
        tmpstr = "\n\nNo More Difference"
        t3.insert(END, tmpstr)

def update():
    analyzer.update_req_text_in_testfile(MyDialog.diffindex)

def result():
    t3.insert(END, "\nGenerating Report ...") 
    report.generate_report()
    t3.insert(END, "\nReport Generated") 


def messageWindow():
    win = Toplevel()
    win.title('warning')
    message = "Do you want to do any action"
    Label(win, text=message).pack()
    Button(win, text='continue', command=win.destroy).pack()


def quit():
    root.destroy()


root.title("RCertif")
#root.attributes('screen', False)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("1000x850+0+0")

index=1
#root.configure(background="gray")

# FRAME=Frame(root, width=100, height =0)
# FRAME.place(x=700,y=0)
#
# LABEL=Label(FRAME, text="test").pack()


#------------------------------------------------------

fm1= Frame (root,width=500, height =900)
fm1.place(x=5,y=20)

t1 = Text(fm1, height=15, width=60, wrap=WORD)
t1.place(x=5,y=65)
quote = "Requirement"
t1.insert(END, quote)

l1=Label(fm1, text="Original requirement text",fg = "lightslategray",font = "Verdana 10 bold")
l1.place(x=5,y=35)


t2= Text(fm1, height=15, width=60, wrap=WORD)
t2.place(x=5,y=355)
# #t2.tag_config('cv',wrap=WORD)
# print(t2.tag_cget('cv','wrap'))
# print("hello")
# #t2.tag_config('cv',wrap=WORD)
# print(t2.tag_cget('cv','wrap'))
quote = "Testplan"
t2.insert(END, quote)

l2=Label(fm1, text="Reference requirement text",fg = "lightslategray",font = "Verdana 10 bold")
l2.place(x=5,y=325)
#-----------------------------------------------------

fm2= Frame (root,width=300, height =600)
fm2.place(x=600,y=20)

t3= Text(fm2, height=550, width=350, wrap=WORD)
t3.place(x=0,y=65)
quote = "Log"
t3.insert(END, quote)
l3=Label(fm2, text="Information",fg = "lightslategray",font = "Verdana 10 bold")
l3.place(x=0,y=35)

#--------------------------------------------------
fm3= Frame (root,width=800, height =1000)
fm3.place(x=200,y=620)

b1 = Button(fm3,text="Analyze",height=2,width=10,command=analyze)
b1.place(x=20,y=60)

b2 = Button(fm3,text="StartDiff",height=2,width=10,command=startdiff)
b2.place(x=110,y=60)

b3 = Button(fm3,text="Previous",height=2,width=10,command=previous)
b3.place(x=200,y=60)

b4 = Button(fm3,text="Next",height=2,width=10,command=next)
b4.place(x=290,y=60)

b5 = Button(fm3,text="Update",height=2,width=10, command=update)
b5.place(x=380,y=60)

b6 = Button(fm3,text="Report",height=2,width=10,command=result)
b6.place(x=470,y=60)

b7 = Button(fm3,text="Exit",height=2,width=10,command=quit)
b7.place(x=560,y=60)

root.mainloop()
