import tkinter as tk
from tkinter import ttk

##help for using  keybinding from this website
##https://www.pythontutorial.net/tkinter/tkinter-event-binding/

window = tk.Tk()
window.title('event')
window.geometry('400x400')

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window,text='click_me')
button.pack()

def get_pos(event):
    print(f'X={event.x} Y={event.y}')
#events
button.bind('<Shift-KeyPress-A>',lambda event:print(event))
##window.bind('<KeyPress>',lambda event:print(f'a button was pressed {event.char}'))

##window.bind('<Motion>',get_pos)

entry.bind('<FocusIn>',lambda event:print('entry filled was selected'))
entry.bind('<FocusOut>',lambda event:print('entry filled was unselected'))

#exercise
text.bind('<Shift-MouseWheel>',lambda event:print('MouseWheel'))

window.mainloop()
