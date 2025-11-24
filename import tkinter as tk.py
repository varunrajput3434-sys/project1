import tkinter as tk
from tkinter import *
expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light blue")
    root.title("Advance  Calculator")
     
   
   
   
   
    root.geometry("270x150")
   
    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=5)

    # Number buttons
    btn1 = Button(root, text='1', fg='blue', bg='white', command=lambda: press(1), height=1, width=5)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='blue', bg='white', command=lambda: press(2), height=1, width=5)  
    btn2.grid(row=2, column=1)
    btn3 = Button(root, text='3', fg='blue', bg='white', command=lambda: press(3), height=1, width=5)
    btn3.grid(row=2, column=2)
    btn4 = Button(root, text='4', fg='blue', bg='white', command=lambda: press(4), height=1, width=5)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='5', fg='blue', bg='white', command=lambda: press(5), height=1, width=5)
    btn5.grid(row=3, column=1)
    btn6 = Button(root, text='6', fg='blue', bg='white', command=lambda: press(6), height=1, width=5)
    btn6.grid(row=3, column=2)
    btn7 = Button(root, text='7', fg='blue', bg='white', command=lambda: press(7), height=1, width=5)
    btn7.grid(row=4, column=0)
    btn8 = Button(root, text='8', fg='blue', bg='white', command=lambda: press(8), height=1, width=5)
    btn8.grid(row=4, column=1)
    btn9 = Button(root, text='9', fg='blue', bg='white', command=lambda: press(9), height=1, width=5)
    btn9.grid(row=4, column=2)
    btn0 = Button(root, text='0', fg='blue', bg='white', command=lambda: press(0), height=1, width=5)
    btn0.grid(row=5, column=0)

    # Operator buttons
    plus = Button(root, text='+', fg='blue', bg='white', command=lambda: press('+'), height=1, width=5)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='blue', bg='white', command=lambda: press('-'), height=1, width=5)
    minus.grid(row=3, column=3)
    mult = Button(root, text='*', fg='blue', bg='white', command=lambda: press('*'), height=1, width=5)
    mult.grid(row=4, column=3)
    div = Button(root, text='/', fg='blue', bg='white', command=lambda: press('/'), height=1, width=5)
    div.grid(row=5, column=3)
    sin = Button(root, text='sin', fg='blue', bg='white', command=lambda: press('sin'), height=1, width=5)
    sin.grid(row=6, column=3)
    cos = Button(root, text='cos', fg='blue', bg='white', command=lambda: press('cos'), height=1, width=5)
    cos.grid(row=6, column=2)
    tan = Button(root, text='tan', fg='blue', bg='white', command=lambda: press('tan'), height=1, width=5)
    tan.grid(row=6, column=1)
    pi = Button(root, text='pi', fg='blue', bg='white', command=lambda: press('pi'), height=1, width=5)
    pi.grid(row=7, column=0)
    In = Button(root, text='In', fg='blue', bg='white', command=lambda: press('In'), height=1, width=5)
    In.grid(row=7, column=1)
    log= Button(root, text='log', fg='blue', bg='white', command=lambda: press('log'), height=1, width=5)
    log.grid(row=7, column=2)
    openbracket  = Button(root, text='(', fg='blue', bg='white', command=lambda: press('('), height=1, width=5)
    openbracket.grid(row=7, column=3)
    closebracket = Button(root, text=')', fg='blue', bg='white', command=lambda: press(')'), height=1, width=5)
    closebracket.grid(row=8, column=0)
    # Other buttons
    eq = Button(root, text='=', fg='blue', bg='white', command=equal, height=1, width=5)
    eq.grid(row=5, column=2)
    clr = Button(root, text='Clear', fg='blue', bg='white', command=clear, height=1, width=5)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', fg='blue', bg='white', command=lambda: press('.'), height=1, width=5)
    dot.grid(row=6, column=0)
   
    root.mainloop()

