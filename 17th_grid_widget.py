import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Grid")
window.geometry('600x600')


label1 = tk.Label(window,text='Label1', background = 'red')
label2 = tk.Label(window, text='Label2',background = 'blue' )
label3 = tk.Label(window, text='Label3', background = 'green')
label4 = tk.Label(window, text='Label4', background='yellow')
button1 = tk.Button(window, text='Button1')
button2 = tk.Button(window, text='Button2')
entry = ttk.Entry(window)

## we can combine row and column or onliner
window.columnconfigure((0,1,2), weight=1, uniform='a')
# define grid
window.columnconfigure(3, weight=2, uniform='a')
##window.columnconfigure(1, weight=1)
##window.columnconfigure(2, weight=1)

window.rowconfigure((0,1,2), weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')
##window.rowconfigure(1,weight=1)

##label1.grid(row=0, column=0, sticky='nsew',padx=20, pady=20,ipadx=30,
##            ipady=50)
##label2.grid(row=1,column=1, sticky='nsew')
##label3.grid(row=2,column=2, columnspan=3,sticky='nsew')
##button1.grid(row=1,column=3,rowspan=4,sticky='nsew')

label1.grid(row=0,column=0, sticky='nsew')
label2.grid(row=1,column=1, rowspan=3,sticky='nsew')
label3.grid(row=1,column=0,sticky='nsew', columnspan=3, padx=20, pady=10)
label4.grid(row=3,column=3, sticky='se')
button1.grid(row=0,column=3, sticky='nsew')
entry.grid(row=3,column=3)
button2.grid(row=2, column=2, sticky='nsew')
window.mainloop()


