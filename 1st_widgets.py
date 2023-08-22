import tkinter as tk
from tkinter import ttk
# open your writeup of tkinter and get some reference
# and also reference from real python tkinter 
def button_func():
    print('button pressed')

def hello():
    print('hello world')
# creating a window
window = tk.Tk()
window.title('1st window')
window.geometry('500x500')
# ttk text
text = tk.Text()
text.pack()
## ttk labels
label = ttk.Label(window, text='this is for text and image widget',foreground='red')
label.pack()
# ttk entry
entry = ttk.Entry(window,)
entry.pack()
#exercise
exer_label = ttk.Label(window,text='my label',foreground='cyan')
exer_label.pack()
##exer_button = ttk.Button(window,text='exer_button',command=hello)
exer_button = ttk.Button(window,text='exer_button',command=lambda:print('hello world'))

exer_button.pack()


# ttk button
button = ttk.Button(window, text='button',command=button_func)
button.pack()





window.mainloop()





#commit this project at end of time
