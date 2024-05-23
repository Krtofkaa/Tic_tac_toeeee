from tkinter import*
from tkinter import messagebox # pazinojumiu iteikumi
mansLogs=Tk()#loga objekts
mansLogs.title("TicTacToe")

btn1=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn2=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn3=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn4=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn5=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn6=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn7=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn8=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))
btn9=Button(mansLogs,text=" ",width=6,height=3,font=("Helvica",24))

btn1.grid(row=0,colum=0)
btn2.grid(row=0,colum=1)
btn3.grid(row=0,colum=2)
btn4.grid(row=1,colum=0)
btn5.grid(row=1,colum=1)
btn6.grid(row=1,colum=2)
btn7.grid(row=2,colum=0)
btn8.grid(row=2,colum=1)
btn9.grid(row=2,colum=2)

mansLogs.mainloop()