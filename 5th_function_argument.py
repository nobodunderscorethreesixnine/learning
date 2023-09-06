import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('function and argument')
window.geometry('400x400')

#without using lambda function
def outer_func(parameter):
    def button_func():
        print('button pressed')
        print(parameter.get())
    return button_func

# no need to learn above code as using lambda function  is easier

def button_func(entry_string):
    print('button pressed')
    print(entry_string.get())



entry_string = tk.StringVar(value='hel')


entry = ttk.Entry(window,textvariable=entry_string)
entry.pack()

button = ttk.Button(window,text='button',
                    #command=lambda:button_func(entry_string)
                    command=outer_func(entry_string)
                    )
button.pack()



window.mainloop()
