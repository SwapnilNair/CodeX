from tkinter import *
import tkinter.font as font
from PIL import ImageTk
from tkinter.font import families
import os
from idlelib.tooltip import Hovertip

#making the root window
root=Tk()
root.geometry('500x510')
root.title(" CodeX ")
#Positioning the image used
photo=PhotoImage(file="/home/swapnil/Projects/CodeX/bg4.png")


#declaring the font look
myFont = font.Font(family='Segoe Script', size=20, weight='bold')

#function to call the C Program
def notepad():
    root.destroy()
    os.system("io.elementary.terminal -e '/home/swapnil/Projects/CodeX/./blue' ")
    #order matters,dont touch this it works
def fchoose():
    os.system("io.elementary.terminal -e 'nautilus'")
   # os.system("io.elementary.terminal -e 'exit' ")
    btn["state"]=NORMAL

#Print the help information here
def hdisplay():
    pass
#The about information here
def adisplay():
    pass

#made a canvas to paste bg on,looks better
canvas=Canvas(width=250,height=350,bg='#8CD3F2')
canvas.pack(expand=YES,fill=BOTH)


#Button formation and placement
btn=Button(root,text="Start CodeX",bg='#303250',fg='white',
                activebackground='#505050',activeforeground='#20FF50',font=(30),command=notepad,cursor='hand2',state=DISABLED)
btn['font'] = myFont
btn.place(x=150,y=120)

#Hover message
myTip=Hovertip(btn,'Please select a file first...',hover_delay=1000)

#Help button
btn2=Button(root,text="Help",bg='#152020',fg='white',
                activebackground='#505050',activeforeground='#00FF50',font=(20),command=hdisplay,cursor='hand2')
btn['font'] = myFont
btn2.place(x=432,y=472)

#about button
btn3=Button(root,text="About",bg='#152020',fg='white',
                activebackground='#505050',activeforeground='#00FF50',font=(20),command=adisplay,cursor='hand2')
btn['font'] = myFont
btn3.place(x=5,y=472)

#File choose
btn4=Button(root,text='Choose File',bg='#303250',fg='white',
                    activebackground='#505050',activeforeground='#00FF50',command=fchoose,cursor='hand2')
btn4.place(x=210,y=180)

#Position canvas and inf loop
#canvas.create_image(640,-20,image=image,anchor=CENTER)  #For Teal
#canvas.create_image(420,200,image=image,anchor=CENTER) #for BW theme
canvas.create_image(300,270,image=photo,anchor=CENTER) #for waves
mainloop()

#101018
#1D4C8B
