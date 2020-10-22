from tkinter import *
import tkinter.filedialog
import os
import pyzipper
import tkinter.messagebox




class Zipsfiles:
    def __init__(self,root):
        self.root=root
        self.root.title("Zip File Extracter")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo155.ico")
        self.root.resizable(0,0)


        filepath=StringVar()
        savefilepath=StringVar()
        password=StringVar()

#===========================================================#

        
        def clear():
            filepath.set("")
            savefilepath.set("")
            password.set("")
            lab_successful.config(text="")

        def findfile():
            a = tkinter.filedialog.askopenfilename(title = "Select file",filetypes = (("Zips","*.zip"),("all files","*.*"))) 
            filepath.set(a)

        def savefile():
            a=tkinter.filedialog.askdirectory(title="choose folder")
            savefilepath.set(a)




        def extracts():
            try:

                if filepath.get()!="":
                    if savefilepath.get()!="":
                        dir_name=filepath.get()
                        with pyzipper.AESZipFile(dir_name) as zf:
                            zf.extractall(path=savefilepath.get())
                            lab_successful.config(text="Successfully Extracted")
                    else:
                        tkinter.messagebox.showerror("Error","Save Path is not defined")

                else:
                    tkinter.messagebox.showerror("Error","File Path is not defined")
            
            except Exception as e:
                tkinter.messagebox.showerror("Error",e)
                lab_successful.config(text="Required Password")





        def extract_password():
            try:

                if filepath.get()!="":
                    if savefilepath.get()!="":                  
                        if password.get()!="":

                            dir_name=filepath.get()
                            with pyzipper.AESZipFile(dir_name) as zf:
                                zf.extractall(path=savefilepath.get(),pwd = bytes(password.get(), 'utf-8'))
                                lab_successful.config(text="Successfully Extracted")

                        else:
                            tkinter.messagebox.showerror("Error","Please Enter the Correct password")
                    else:
                        tkinter.messagebox.showerror("Error","Save Path is not defined")

                else:
                    tkinter.messagebox.showerror("Error","File Path is not defined")
            
            except Exception as e:
                tkinter.messagebox.showerror("Error",e)
                lab_successful.config(text="Incorrect Password")


            




#===========================================================#
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=300,relief="ridge",bd=3,bg="#312244")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=93,relief="ridge",bd=3,bg="#354f52")
        secondframe.place(x=0,y=300)

#=============================================================#
        but_extract=Button(secondframe,width=14,text="Extract",font=('times new roman',12),cursor="hand2",command=extracts)
        but_extract.place(x=20,y=30)

        but_extract_password=Button(secondframe,width=14,text="Extract-Password",font=('times new roman',12),cursor="hand2",command=extract_password)
        but_extract_password.place(x=175,y=30)
        
        but_clear=Button(secondframe,width=14,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=330,y=30)
#==================================================================#

        but_find_file=Button(firstframe,width=14,text="Find File",font=('times new roman',12),cursor="hand2",command=findfile)
        but_find_file.place(x=175,y=10)

        ent_file=Entry(firstframe,width=50,font=('times new roman',12),relief="ridge",bd=3,textvariable=filepath)
        ent_file.place(x=40,y=60)

        but_find_savefile=Button(firstframe,width=14,text="Save to Folder",font=('times new roman',12),cursor="hand2",command=savefile)
        but_find_savefile.place(x=175,y=120)

        ent_file=Entry(firstframe,width=50,font=('times new roman',12),relief="ridge",bd=3,textvariable=savefilepath)
        ent_file.place(x=40,y=160)

        lab_password=Label(firstframe,text="Enter Password",font=('times new roman',12),bg="#312244",fg="white")
        lab_password.place(x=70,y=230)

        ent_file=Entry(firstframe,width=24,font=('times new roman',12),relief="ridge",bd=3,textvariable=password)
        ent_file.place(x=200,y=230)

        lab_successful=Label(firstframe,text="",font=('times new roman',12),bg="#312244",fg="white")
        lab_successful.place(x=200,y=265)

     
if __name__ == "__main__":
    root=Tk()
    app=Zipsfiles(root)
    root.mainloop()