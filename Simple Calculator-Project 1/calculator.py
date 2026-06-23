from tkinter import *
win = Tk()

data = ""
vars = StringVar()

def get_data(value):
    global data
    data = data + str(value)
    vars.set(data)


def equal_data():
    global data
   
    try:
        result = str(eval(data))
        data = result
        vars.set(result)
   
    except Exception:
        data = ""
        vars.set("Error")


def clear():
    global data
    data = ""
    vars.set("")
    
win.title("Calculator")
win.geometry("350x500")
win.config(bg="lightgrey")
win.resizable(False, False)

label_title = Label(win, text="CALCULATOR", font=("Berlin Sans FB", 32, "bold"), bg="lightgrey", fg="black")
label_title.pack(pady=2,padx=5,fill=X)

entry=Entry(win, font=("Times New Roman", 20), bd=6, relief=RIDGE, justify=RIGHT ,textvariable=vars) 
entry.pack(pady=10, padx=5,fill=X)

button_1 = Button(win, text="1", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(1))
button_1.place(x=20, y=350, width=70, height=50)

button_2 = Button(win, text="2", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(2))
button_2.place(x=100, y=350, width=70, height=50)

button_3 = Button(win, text="3", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(3))
button_3.place(x=180, y=350, width=70, height=50)

button_4 = Button(win, text="4", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(4))
button_4.place(x=20, y=280, width=70, height=50)

button_5 = Button(win, text="5", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(5))
button_5.place(x=100, y=280, width=70, height=50)

button_6 = Button(win, text="6", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(6))       
button_6.place(x=180, y=280, width=70, height=50)

button_7 = Button(win, text="7", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(7))
button_7.place(x=20, y=210, width=70, height=50)

button_8 = Button(win, text="8", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(8))
button_8.place(x=100, y=210, width=70, height=50)

button_9 = Button(win, text="9", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(9))
button_9.place(x=180, y=210, width=70, height=50)

button_0 = Button(win, text="0", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(0))
button_0.place(x=100, y=420, width=70, height=50)

button_plus = Button(win, text="+", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data("+"))
button_plus.place(x=260, y=350, width=70, height=50)

button_minus = Button(win, text="-", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data("-"))
button_minus.place(x=260, y=280, width=70, height=50)

button_multiply = Button(win, text="*", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data("*"))
button_multiply.place(x=260, y=210, width=70, height=50)

button_divide = Button(win, text="/", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data("/"))
button_divide.place(x=260, y=140, width=70, height=50)

button_clear = Button(win, text="C", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=clear)
button_clear.place(x=180, y=140, width=70, height=50)

button_equal = Button(win, text="=", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=equal_data)
button_equal.place(x=260, y=420, width=70, height=50)

button_dot = Button(win, text=".", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data("."))
button_dot.place(x=180, y=420, width=70, height=50)

button_open_bracket = Button(win, text="(", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data("("))
button_open_bracket.place(x=20, y=140, width=70, height=50)

button_close_bracket = Button(win, text=")", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data(")"))
button_close_bracket.place(x=100, y=140, width=70, height=50)

button_modulo = Button(win, text="%", font=("Times New Roman", 20), bd=6, relief=RIDGE, command=lambda: get_data("%"))
button_modulo.place(x=20, y=420, width=70, height=50)


win.mainloop()
