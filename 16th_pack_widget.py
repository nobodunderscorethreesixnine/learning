#.pack()

'''pack options .pack(side=top/left,right,bottom,#top is default value of side
                    expand=True/False)#define vertical or horizontal space a widget
                                        can occupy
                    fill=tk.X/X/BOTH/None #fill the space that expand options will
                                            define
                    pady=20
                    padx=30

                    #ipady and ipadx are for internal padding
                    ipady=20
                    ipadx=20
                    '''

#exercise
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('exercise')
window.geometry('500x500')

label1 = tk.Label(window, text='label 1', background='red')

label2 = tk.Label(window, text='label 2', background='blue' )
label3 = tk.Label(window, text='label 3', background='green' )
button = tk.Button(window, text='label 4', background='lightgrey')

#packing
label1.pack(expand=True,fill=tk.BOTH, pady=10, padx=10)
label2.pack(expand=True,side='left', fill=tk.BOTH)
label3.pack(expand=True, fill=tk.BOTH)
button.pack(expand=True, fill=tk.BOTH)

window.mainloop()

'pack + frame'

start from 4:46:41
