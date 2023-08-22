import tkinter as tk
from tkinter import ttk
##import ttkbootstrap as ttk #same as ttk but add more design by default
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    
##    print(entry_int.get())
    output_string.set(km_output)



#window

window = tk.Tk()
window.title("tk")
window.geometry('500x500')

##title_label = ttk.Label(master=window)
title_label = tk.Label(master=window, text='miles to kilometer', font='calibri 24 underline')
title_label.pack()

input_frame = ttk.Frame(window)
entry_int = tk.IntVar()
entry= ttk.Entry(input_frame, textvariable=entry_int)
button= ttk.Button(input_frame, text='convert',command=convert)

entry.pack(side='left',padx=20)
button.pack(side='left')

input_frame.pack(pady=20)

#output
output_string = tk.StringVar()
output_label = ttk.Label(window,text='output',
                         font='calibri 24 italic',textvariable=output_string)
output_label.pack()

