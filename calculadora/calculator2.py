#Gabriel Campos Amaral Ribeiro
#18/07/2023

#Calculadora com botoes interativos


import tkinter as tk

from tkinter import *
from tkinter import ttk




#Cria a janela
janela=tk.Tk()
#Define o nome para a janela
janela.title('Calculator')
#Define o tamanho da tela
janela.geometry('223x340')
#Impede que a janela mude de tamanho
janela.resizable(False,False)

#Cria o visor
frame=Frame(janela,bg="#38576b",width=300,height=70)
frame.grid(row=0,column=0)

#Frame onde vao os numeros
frameCorpo=Frame(janela,bg="#ECEFF1",width=300,height=385)
frameCorpo.grid(row=2,column=0)


equation=''

def show(value):
    global equation
    equation+=value
    app.config(text=equation)


def clear():
    global equation
    equation=''
    app.config(text=equation)




#Visor funcional
val=StringVar()
app=Label(frame,textvariable=val,width=16,height=3,padx=7,relief=FLAT,anchor='e',justify=RIGHT,font=('Ivy 16 bold'),bg="#38576b",fg='white')
app.place(x=0,y=0)


#Botoes
b1=Button(frameCorpo,text='C',width=14,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:clear())
b1.place(x=0,y=0)

b2=Button(frameCorpo,text='%',width=5,height=2,bg='#FFAB40',fg='white',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b2.place(x=118,y=0)

b3=Button(frameCorpo,text='/',width=5,height=2,bg='#FFAB40',fg='white',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:show('/'))
b3.place(x=177,y=0)

b4=Button(frameCorpo,text='7',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b4.place(x=0,y=52)

b5=Button(frameCorpo,text='8',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b5.place(x=59,y=52)

b6=Button(frameCorpo,text='9',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b6.place(x=118,y=52)

b7=Button(frameCorpo,text='*',width=5,height=2,bg='#FFAB40',fg='white',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b7.place(x=177,y=52)

b8=Button(frameCorpo,text='4',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b8.place(x=0,y=104)

b9=Button(frameCorpo,text='5',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b9.place(x=59,y=104)

b10=Button(frameCorpo,text='6',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b10.place(x=118,y=104)

b11=Button(frameCorpo,text='-',width=5,height=2,bg='#FFAB40',fg='white',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b11.place(x=177,y=104)

b12=Button(frameCorpo,text='1',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b12.place(x=0,y=160)

b13=Button(frameCorpo,text='2',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b13.place(x=59,y=160)

b14=Button(frameCorpo,text='3',width=5,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b14.place(x=118,y=160)

b15=Button(frameCorpo,text='+',width=5,height=2,bg='#FFAB40',fg='white',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b15.place(x=177,y=160)

b16=Button(frameCorpo,text='0',width=14,height=2,bg='white',fg='black',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b16.place(x=0,y=215)

b17=Button(frameCorpo,text='.',width=5,height=2,bg='#FFAB40',fg='white',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b17.place(x=118,y=215)

b18=Button(frameCorpo,text='=',width=5,height=2,bg='#FFAB40',fg='white',font=('Ivy 9 bold'),relief=RAISED,overrelief=RIDGE)
b18.place(x=177,y=215)











#Permite a janela ficar aberta
janela.mainloop()