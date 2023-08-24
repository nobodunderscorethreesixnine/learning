import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()
    #updating label by config() or configure() or [] method
##  label.config(text=entry.get())
    label['text'] = entry_text
    entry['state'] = 'disabled'
##    print(button.config())

def reset_func():
##    label['text'] = 'some text'
##    label.configure(text='some text')
    label['text']='some text'
##    entry['state']='enabled'
    entry.config(state='enabled')
##    label.config(state='enabled')

window = tk.Tk()
window.title('Getting and setting widget')
window.geometry('400x400')

#widgets
label = ttk.Label(window, text='some text')
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window,text='click_me',command=button_func)
button.pack()

exr_reset_btn = ttk.Button(window, text='reset',command=reset_func)
exr_reset_btn.pack()

window.mainloop()
