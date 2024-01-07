#simple calculator

from tkinter import *

obj = Tk()
obj.geometry("313x350")
obj.resizable(False, False)
obj.configure(bg="#000000")
obj.title("Simple Calculator")

equation = ""

def show(value):
    global equation
    equation += value
    result.config(text=equation)

def clear():
    global equation
    equation = ""
    result.config(text=equation)

def calculate():
    global equation
    if result != "":
        try:
            result1 = eval(equation)
        except:
            result1 = "error"
            equation = ""
        result.config(text=result1)

result = Label(obj, height=3, width=39, fg="white", bg="black", font=("arial"), cursor="ibeam")
result.place(x=0, y=0)

Button(obj, text="C", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#64dd17",
       command=lambda: clear()).place(x=10, y=95)
Button(obj, text=".", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show(".")).place(x=85, y=95)
Button(obj, text="%", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("%")).place(x=160, y=95)
Button(obj, text="/", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#f57c00",
       command=lambda: show("/")).place(x=235, y=95)

Button(obj, text="7", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("7")).place(x=10, y=145)
Button(obj, text="8", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("8")).place(x=85, y=145)
Button(obj, text="9", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("9")).place(x=160, y=145)
Button(obj, text="*", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#f57c00",
       command=lambda: show("*")).place(x=235, y=145)

Button(obj, text="4", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("4")).place(x=10, y=195)
Button(obj, text="5", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("5")).place(x=85, y=195)
Button(obj, text="6", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("6")).place(x=160, y=195)
Button(obj, text="+", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#f57c00",
       command=lambda: show("+")).place(x=235, y=195)

Button(obj, text="1", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("1")).place(x=10, y=245)
Button(obj, text="2", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("2")).place(x=85, y=245)
Button(obj, text="3", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("3")).place(x=160, y=245)
Button(obj, text="-", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#f57c00",
       command=lambda: show("-")).place(x=235, y=245)

Button(obj, text="0", width=5, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#424242",
       command=lambda: show("0")).place(x=10, y=295)
Button(obj, text="=", width=17, height=1, font=("arial", 15, "bold"), bd=2, fg="#ffffff", bg="#00b0ff",
       command=lambda: calculate()).place(x=88, y=295)

obj.mainloop()