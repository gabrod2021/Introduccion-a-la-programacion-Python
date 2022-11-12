from distutils.cygwinccompiler import CygwinCCompiler
import tkinter
from tkinter import W, Tk, ttk
from click import command
from numpy import expand_dims
from sqlalchemy import column


window = tkinter.Tk()


window['bg']='lightblue'
#pass_Entry=ttk.Entry(window,show="*")
label=tkinter.Label(window,text="",bg="lightblue")
label.grid(column=1,row=0,sticky="W")
label1=tkinter.Label(window,text="Marca los paises para los que trabajarias: ",bg="lightblue",fg="black")
label1.grid(column=0,row=1,sticky="W")
label2=tkinter.Label(window,text=" Elije uno o mas idiomas: ",bg="lightblue",fg="black")
label2.grid(column=0,row=8,rowspan=True,sticky="W")
label4=tkinter.Label(window,text="Podrias trasladarte?:",bg="lightblue",fg="black")
label4.grid(column=1,row=2,rowspan=True,sticky="W")
label4=tkinter.Label(window,text="Marca tu area de desempeño:",bg="lightblue",fg="black")
label4.grid(column=1,row=4,rowspan=True,sticky="W")

selected = tkinter.IntVar() 

combo = ttk.Combobox(state="readonly",
values=["SI","NO", "TAL VEZ",""])
combo.grid(column=1,row=3,sticky="W") 
rOne = tkinter.Checkbutton(window, text='Argentina',pady=5,padx=20) 
rTwo = tkinter.Checkbutton(window, text='USA',pady=5,padx=20) 
rThree = tkinter.Checkbutton(window, text='Reino Unido',pady=5,padx=20)
rFour = tkinter.Checkbutton(window, text='Suiza',pady=5,padx=20) 
rFive = tkinter.Checkbutton(window, text='Brasil',pady=5,padx=20) 
rSix = tkinter.Checkbutton(window, text='Paraguay',pady=5,padx=20)

listbox = tkinter.Listbox(selectmode=tkinter.EXTENDED,height=6)
items = [
    " Ingles",
    " Español",
    " Aleman",
    " Portugues",
    " Guaraní"

]
listbox.insert(0, *items)
listbox.grid(column=0,rowspan=9,sticky="W")

selected = tkinter.IntVar() 

 
uno = tkinter.Radiobutton(window, text='Programador Front End',variable=selected, value=1,pady=2,padx=20) 
dos = tkinter.Radiobutton(window, text='Testing QA',variable=selected, value=2,pady=2,padx=20) 
tres= tkinter.Radiobutton(window, text='Data Analitics',variable=selected, value=3,pady=2,padx=20)
cuatro = tkinter.Radiobutton(window, text='Programador Back End',variable=selected, value=4,pady=2,padx=20) 
cinco = tkinter.Radiobutton(window, text='Full Stack ',variable=selected, value=5,pady=2,padx=20) 
seis = tkinter.Radiobutton(window, text='Analista tecnico',variable=selected, value=6,pady=2,padx=20)

rOne["bg"]="lightblue"
rOne["fg"]="magenta"
rTwo["bg"]="lightblue"
rTwo["fg"]="magenta"
rThree["bg"]="lightblue"
rThree["fg"]="magenta"
rFour["bg"]="lightblue"
rFour["fg"]="magenta"
rFive["bg"]="lightblue"
rFive["fg"]="magenta"
rSix["bg"]="lightblue"
rSix["fg"]="magenta"


rOne.grid(column=0, row=2,sticky="W")
rTwo.grid(column=0, row=3,sticky="W")
rThree.grid(column=0, row=4,sticky="W")
rFour.grid(column=0, row=5,sticky="W")
rFive.grid(column=0, row=6,sticky="W")
rSix.grid(column=0, row=7,sticky="W")


uno.grid(column=1, row=5,sticky="W")
dos.grid(column=1, row=6,sticky="W")
tres.grid(column=1, row=7,sticky="W")
cuatro.grid(column=1, row=8,sticky="W")
cinco.grid(column=1, row=9,sticky="W")
seis.grid(column=1, row=10,sticky="W")




window.mainloop()