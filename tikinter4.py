from tkinter import *
root = Tk()
class MyDialog:
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

def onClick():
    inputDialog = MyDialog(root)
    root.wait_window(inputDialog.top)
    print('Response: ', response)
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


#root.configure(background="gray")

# FRAME=Frame(root, width=100, height =0)
# FRAME.place(x=700,y=0)
#
# LABEL=Label(FRAME, text="test").pack()


#------------------------------------------------------
fm1= Frame (root,width=500, height =900)
fm1.place(x=5,y=20)

t1 = Text(fm1, height=15, width=100)
t1.place(x=5,y=65)
quote = "Requirement"
t1.insert(END, quote)

l1=Label(fm1, text="Original requirement text",fg = "lightslategray",font = "Verdana 10 bold")
l1.place(x=5,y=35)


t2= Text(fm1, height=15, width=100)
t2.place(x=5,y=355)
quote = "Testplan"
t2.insert(END, quote)

l2=Label(fm1, text="Reference requirement text",fg = "lightslategray",font = "Verdana 10 bold")
l2.place(x=5,y=325)
#-----------------------------------------------------

fm2= Frame (root,width=300, height =600)
fm2.place(x=600,y=20)

t3= Text(fm2, height=550, width=350)
t3.place(x=0,y=65)
quote = "Log"
t3.insert(END, quote)
l3=Label(fm2, text="Information",fg = "lightslategray",font = "Verdana 10 bold")
l3.place(x=0,y=35)

#--------------------------------------------------
fm3= Frame (root,width=500, height =300)
fm3.place(x=200,y=620)

b1 = Button(fm3,text="Action",height=2,width=10,command=messageWindow)
b1.place(x=20,y=60)

b2 = Button(fm3,text="Response",height=2,width=10,command=onClick)
b2.place(x=110,y=60)

b3 = Button(fm3,text="task",height=2,width=10)
b3.place(x=200,y=60)

b4 = Button(fm3,text="start",height=2,width=10)
b4.place(x=290,y=60)

b5 = Button(fm3,text="Exit",height=2,width=10,command=quit)
b5.place(x=380,y=60)

root.mainloop()
