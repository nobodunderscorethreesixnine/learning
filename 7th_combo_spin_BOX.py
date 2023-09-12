import tkinter as tk
from tkinter import ttk

##https://www.pythontutorial.net/tkinter/tkinter-event-binding/

window = tk.Tk()
window.title('combo and spin box')
window.geometry('400x400')

#combox
# to use Combobox use ttk , it is not availabel in tk
items = ('Ice cream', 'Pizza','Broccoli')
food_strings = tk.StringVar(value = items[2])
combo = ttk.Combobox(window,textvariable=food_strings,values=items)
# for below 2 line u can direct use value in above      \\
combo['values'] = items #try to use this then configure/config
##combo.configure(values=items)
combo.pack()

#events
combo.bind("<<ComboboxSelected>>",
lambda event:combo_label.configure(text=f'user selected {food_strings.get()}'))
#their is no command  param in up

combo_label = ttk.Label(window,text='a label') #it can be null also
combo_label.pack()

#Spinbox
spinbox_var = tk.IntVar(value=6)
spinbox = ttk.Spinbox(window,from_ =3,#dont forget _ in from_
                      to=20,increment=3, textvariable=spinbox_var,
            command=lambda :print(spinbox_var.get()))#not need event param
##spinbox['value']=(1,2,3,4,5)
spinbox.pack()

spinbox.bind('<<Increment>>',lambda event:print('up'))
spinbox.bind('<<Decrement>>',lambda event:print('down'))

#exercise
spin_letters = ('A','B','C','D','E')

spin_var= tk.StringVar(value=spin_letters[0])
spinbox = ttk.Spinbox(window,textvariable=spin_var,values=spin_letters)
##spinbox['values'] = spin_letters #('A','B','C','D','E')
spinbox.pack()
#event
spinbox.bind('<<Decrement>>',lambda event:print(spin_var.get()))

window.mainloop()

window.mainloop()
