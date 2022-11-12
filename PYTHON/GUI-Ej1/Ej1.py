
import tkinter
from tkinter import ttk
from click import command

def reset(event):
  selected.set("Animate con uno!")

    
window = tkinter.Tk()

window['bg']='black'

label=tkinter.Label(window,text="",bg="black")
label.grid(column=1,row=0,sticky="W")
label=tkinter.Label(window,text="SELECCIONA TU CURSO!",bg="black",fg="white")
label.grid(column=0,row=1,sticky="W")
label=tkinter.Label(window,text="Tu curso es el N°:",bg="black",fg="white")
label.grid(column=1,row=2)

selected = tkinter.IntVar() 

 
rOne = tkinter.Radiobutton(window, text='Python',variable=selected, value=1,pady=5,padx=20) 
rTwo = tkinter.Radiobutton(window, text='Java',variable=selected, value=2,pady=5,padx=20) 
rThree = tkinter.Radiobutton(window, text='Javascript',variable=selected, value=3,pady=5,padx=20)
rFour = tkinter.Radiobutton(window, text='Django',variable=selected, value=4,pady=5,padx=20) 
rFive = tkinter.Radiobutton(window, text='Spring',variable=selected, value=5,pady=5,padx=20) 
rSix = tkinter.Radiobutton(window, text='MySql',variable=selected, value=6,pady=5,padx=20)

rOne["bg"]="black"
rOne["fg"]="magenta"
rTwo["bg"]="black"
rTwo["fg"]="magenta"
rThree["bg"]="black"
rThree["fg"]="magenta"
rFour["bg"]="black"
rFour["fg"]="magenta"
rFive["bg"]="black"
rFive["fg"]="magenta"
rSix["bg"]="black"
rSix["fg"]="magenta"


boton=tkinter.Button(window,text="Reset")
boton.grid(row=7,column=2,padx=30)
boton.bind("<Button-1>",reset)
boton["bg"]="yellow"


rOne.grid(column=0, row=2,sticky="W")
rTwo.grid(column=0, row=3,sticky="W")
rThree.grid(column=0, row=4,sticky="W")
rFour.grid(column=0, row=5,sticky="W")
rFive.grid(column=0, row=6,sticky="W")
rSix.grid(column=0, row=7,sticky="W")
label=tkinter.Label(window,text="",bg="black")
label.grid(column=0,row=8,sticky="W")


labelValue = tkinter.Label(window, textvariable=selected)
labelValue.grid(column=2, row=2, sticky="W", padx=30)
labelValue["bg"]="lightgreen"


window.mainloop()