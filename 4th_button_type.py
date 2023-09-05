import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('button')
window.geometry('400x400')

# types of button - button,checkbutton,radiobutton
def button_func():
##    print('hello world')
    print(check_var)
    print(radio_var.get())
button_var = tk.StringVar(value='simple button')
button = ttk.Button(window,text='simple button', textvariable=button_var
                    ,command = lambda:print('hello world'))
button.pack()

#check button
check_var = tk.StringVar(value=100) #variable to check if tick or not. -StringVar/IntVar both work

check = ttk.Checkbutton(window,text='checkbox',command=lambda:print(check_var.get()),
                        variable=check_var,
                        onvalue=100,
                        offvalue=1) #textvariable is only "variable" here
#onvalue and offvalue is for custom checking tick or not tick.
check.pack()

# radio button
radio_var = tk.StringVar()


radio1 = ttk.Radiobutton(window,text='Radiobutton 1',value='radio 1',
                         variable=radio_var)
radio1.pack()

radio2 = ttk.Radiobutton(window,text='Radiobutton 2',value =2,variable=radio_var
                         ,command=lambda:print(radio_var.get()))
radio2.pack()

#exercise
# check button
check_btn_var = tk.BooleanVar(value='false')
check_btn = ttk.Checkbutton(window,variable=check_btn_var,
                            onvalue='true',offvalue='false',
                            command=lambda:print(radio_var.get()))

check_btn.pack()
print(check_btn_var.get())

#radio button
radio_var = tk.StringVar()
def radio_func():
    print(check_btn_var.get())
    check_btn_var.set('false')
radio1 = ttk.Radiobutton(window,text='radio 1',value='a',variable=radio_var,
                         command=radio_func)
radio1.pack()

radio2 = ttk.Radiobutton(window,text='radio 2',value='b',variable=radio_var,
                         command=radio_func)
radio2.pack()

