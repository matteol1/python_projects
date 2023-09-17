import tkinter as tk

global first_factor
global operation

def button_add():
    global first_factor
    first_factor = float(en.get())
    global operation
    operation = "addition"
    en.delete(0,'end')

def button_subtract():
    global first_factor
    first_factor= float(en.get())
    global operation
    operation = "subtraction"
    en.delete(0,'end')

def button_multiply():
    global first_factor
    first_factor= float(en.get())
    global operation
    operation = "multiplication"
    en.delete(0,'end')

def button_divide():
    global first_factor
    first_factor= float(en.get())
    global operation
    operation = "division"
    en.delete(0,'end')

def button_equal():
    second_factor = float(en.get())
    en.delete(0,'end')
    if operation == "addition":
        en.insert(0, first_factor + second_factor)
    elif operation == "subtraction":
        en.insert(0, first_factor - second_factor)
    elif operation == "multiplication":
        en.insert(0, first_factor * second_factor)
    elif operation == "division":
        en.insert(0, first_factor / second_factor)


def button_clear():
    en.delete(0, 'end')

def button_click(number):
    tmp = en.get()
    en.delete(0, 'end')
    en.insert(0, str(tmp) + str(number))

def button_period():
    tmp = str(en.get())
    if tmp.find('.')==-1:
    #en.insert('end', en.get('end'))
        en.insert('end', ".")


root = tk.Tk()
root.geometry("500x300")
root.title("My Calculator")

#frame = tk.Frame(root, bg="black")
#frame.pack()

en = tk.Entry(root)#, bg="#FF0000")
en.grid(row=0,column=0, columnspan=4)
        
buttonadd = tk.Button(master=root, text="+", command=button_add)
buttonadd.grid(row=5,column=3, padx=12,pady=10)
buttonsub = tk.Button(master=root, text="-", command=button_subtract)
buttonsub.grid(row=4,column=3, padx=12,pady=10)
buttonmul = tk.Button(master=root, text="*", command=button_multiply)
buttonmul.grid(row=3,column=3, padx=12,pady=10)
buttondiv = tk.Button(master=root, text="/", command=button_divide)
buttondiv.grid(row=2,column=3, padx=12,pady=10)

buttonequal = tk.Button(master=root, text="=", command=button_equal)
buttonequal.grid(row=3,column=4, padx=30,pady=10)
buttonclaar = tk.Button(master=root, text="Clear", command=button_clear)
buttonclaar.grid(row=2,column=4, padx=30,pady=10)


button1 = tk.Button(master=root, text="1", command=lambda: button_click(1))
button1.grid(row=4,column=0, padx=12,pady=10)
button2 = tk.Button(master=root, text="2", command=lambda: button_click(2))
button2.grid(row=4,column=1, padx=12,pady=10)
button3 = tk.Button(master=root, text="3", command=lambda: button_click(3))
button3.grid(row=4,column=2, padx=12,pady=10)
button4 = tk.Button(master=root, text="4", command=lambda: button_click(4))
button4.grid(row=3,column=0, padx=12,pady=10)
button5 = tk.Button(master=root, text="5", command=lambda: button_click(5))
button5.grid(row=3,column=1, padx=12,pady=10)
button6 = tk.Button(master=root, text="6", command=lambda: button_click(6))
button6.grid(row=3,column=2, padx=12,pady=10)
button7 = tk.Button(master=root, text="7", command=lambda: button_click(7))
button7.grid(row=2,column=0, padx=12,pady=10)
button8 = tk.Button(master=root, text="8", command=lambda: button_click(8))
button8.grid(row=2,column=1, padx=12,pady=10)
button9 = tk.Button(master=root, text="9", command=lambda: button_click(9))
button9.grid(row=2,column=2, padx=12,pady=10)
button0 = tk.Button(master=root, text="0", command=lambda: button_click(0))
button0.grid(row=5,column=1, padx=12,pady=10)
button0 = tk.Button(master=root, text=".", command=button_period)
button0.grid(row=5,column=2, padx=12,pady=10)



#frame = tkinter.Frame(master=mygui)
#frame.pack(pady=20,padx=60,fill="both",expand=False,)
#

root.mainloop()