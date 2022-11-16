from tkinter import *
from googletrans import Translator,LANGUAGES
from tkinter import ttk
root=Tk()
root.geometry("900x300")
root.config(bg="#F2CCC3")

label=Label(root,text="LANGUAGE TRANSLATOR",bg = "#F2CCC3",font=("Bahnschrift light",15))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text=Label(root,text="Enter Text",bg = "#F2CCC3",font=("Bahnschrift light",10))
text.place(relx=0.02,rely=0.2,anchor=W)

area=Text(root,bg = "white",font=("Bahnschrift light",10),wrap=WORD,height=10,width=50,bd=0)
area.place(relx=0.02,rely=0.4,anchor=W)
language=list(LANGUAGES.values())
box=ttk.Combobox(root,state="readonly",values=language,width="30")
box.set("english")
box.place(relx=0.1,rely=0.2,anchor=W)

otext=Label(root,text="Output",bg = "#F2CCC3",font=("Bahnschrift light",10))
otext.place(relx=0.71,rely=0.2,anchor=E)

oarea=Text(root,bg = "white",font=("Bahnschrift light",10),wrap=WORD,height=10,width=50,bd=0)
oarea.place(relx=0.99,rely=0.4,anchor=E)
language=list(LANGUAGES.values())
obox=ttk.Combobox(root,state="readonly",values=language,width="30")
obox.set("english")
obox.place(relx=0.98,rely=0.2,anchor=E)

button=Button(root,text="translate",font=("Bahnschrift light",10),bg="#F2CCC3",activebackground="white",fg="black",relief="flat")
button.place(relx=0.5,rely=0.55,anchor=CENTER)

root.mainloop()