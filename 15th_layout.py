import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('layout intro')
window.geometry('500x500')


# widgets
label1 = tk.Label(window, text='label 1 ', background='red')
label2 = tk.Label(window, text='label 2', background='blue')

'pack'
#label1.pack(side='left', expand=True, fill=tk.X) #fill=tk.X/Y/BOTH
#label2.pack(side='left', expand=True, fill=tk.BOTH)
''' expand=True will expand the widget meaning it place gap between two widgets
    and if fill is define then it will fill the gap with color '''

'grid'
'''
window.columnconfigure(0, weight=1)
window.columnconfigure(1 , weight=1)
window.columnconfigure(2, weight=2)
window.rowconfigure(0, weight=1)

label1.grid(row=0, column=0 , sticky='ewsn') #w=left,e=right,s=down,north=up
label2.grid(row=0, column=1, sticky='ewsn')
'''

'place'
#label1.place(x=200, y=200, width=200, height=200)
#label2.place(relx=0.5, rely=0.5, anchor='center'#anchor=ne/nw/se/sw/center
#             ,relwidth=1)#all relx/y/width will be on decimal(0.0to1)

window.mainloop()


