import tkinter as tk
from tkinter import ttk

# additional methods are found here
#https://www.tutorialspoint.com/python/tk_menu.htm

window = tk.Tk()
window.title('Menu')
window.geometry('500x500')

#menu
menu = tk.Menu(window)

#sub-menu
file_menu = tk.Menu(menu)
#
file_menu.add_command(label='New', command=lambda:print('creating new file'))
file_menu.add_command(label='Open', command=lambda:print('opening file'))
menu.add_cascade(label='File', menu=file_menu)

file_menu.add_separator()

#another sub-menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help', command=lambda:print('beg for help'))


help_menu_var = tk.StringVar()
help_menu.add_checkbutton(label='check', onvalue='on', offvalue='off',
                          variable=help_menu_var,
                          command=lambda:print(help_menu_var.get()))



menu.add_cascade(label='Help', menu=help_menu)

# Exercise #another sub-menu
exercise_menu = tk.Menu(menu , tearoff=False)
exercise_menu.add_command(label='exer' ,)#if u want no need to add commnad always

setting_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_cascade(label='settings',menu=setting_menu)
setting_menu.add_command(label='preferences',command=lambda:print('it fuckin works'))




menu.add_cascade(label='Exercise', menu=exercise_menu)


window.configure(menu=menu)

# menu button  'this is different from above'
menuButton = ttk.Menubutton(window, text='menu')
menuButton.pack()

button_sub_menu = tk.Menu(menuButton, tearoff=False)
button_sub_menu.add_command(label='?', command=lambda:print('? WTF'))
button_sub_menu.add_checkbutton(label='/', command=lambda:print('/ WTF'))

menuButton.configure(menu=button_sub_menu)
##menuButton['menu'] = button_sub_menu

window.mainloop()
