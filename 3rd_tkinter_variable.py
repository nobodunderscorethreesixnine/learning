import tkinter as tk
from tkinter import ttk

#func
def button_func():
    print(string_variable.get())
    string_variable.set('button pressed')


window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('400x400')

#tkinter variables
# types of variabes = tk.StringVar/IntVar/DoubleVar/Booleanvar
string_variable = tk.StringVar(value='this is for start variable')

#widgets
label = ttk.Label(window,text='label', textvariable=string_variable)
label.pack()

entry = ttk.Entry(window, textvariable=string_variable)
entry.pack()

entry2 = ttk.Entry(window, textvariable=string_variable)
entry2.pack()

button = ttk.Button(window, text='button', command=button_func)
button.pack()

exer_string_var = tk.StringVar(value='this is for start value')

exer_label = ttk.Label(window,text='hello',textvariable=exer_string_var)
exer_label.pack()
exer_entry = ttk.Entry(window,textvariable=exer_string_var)
exer_entry.pack()

exer_entry2 = ttk.Entry(window,textvariable=exer_string_var)
exer_entry2.pack()





#run
window.mainloop()
