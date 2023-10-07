import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x600')
window.title('Tab widget')

# Notebook widget
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
#putting widget or text inside tab1
label = ttk.Label(tab1,text='inside only of tab1')
label.pack()

button = ttk.Button(tab1,text='inside tab 1')
button.pack()

tab2 = ttk.Frame(notebook)
#putting widget or text inside tab2
label = ttk.Label(tab2,text='inside only of tab2')
label.pack()

entry = tk.Entry(tab2)
entry.pack()

tab3 = ttk.Frame(notebook)
#putting widget or text inside tab3
text = tk.Text(tab3)
text.pack()


tk.Button(tab3, text='Submit').pack() #u can use one liner also

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')

notebook.pack(side='bottom')

#exercise

exer_notebook = ttk.Notebook(window)

#tabs
exer_tab1 = ttk.Frame(exer_notebook)
#putting  below widget inside exer_tab1
button = ttk.Button(exer_tab1,text='exer_button')
button.pack()

exer_tab2 = ttk.Frame(exer_notebook)
#putting below widget inside exer_tab2
tk.Entry(exer_tab2,).pack()

#packing both tab **note here with notebook.add()=>func()
exer_notebook.add(exer_tab1, text='exer_tab1')
exer_notebook.add(exer_tab2, text='exer_tab2')

exer_notebook.pack()

window.mainloop()
