import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('more on window')

#window.geometry('500x600+0+0') #+500+200 = left+top it configures where to
'exercise' # to center the window
window_width = 500
window_height = 500
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2) #470
top = int(display_height / 2 - window_height / 2) #200
''' left and top should be convert to int otherwise,window.geometry() doesn't
    support float '''
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

#place window

window.iconbitmap('joker.ico') # to put your own logo in window PS:convert png to.ico file_ext

##window.minsize(200,200)#width,height# window will not able to  shrink buy user from 
#200width and 200height

##window.maxsize(800,800)#width,height# window can be expand upto 800width and 800height
#by user

window.resizable(True,False)#x-dimension , y-dimension if x true then x can be
#resizable else viceversa

#PS mainly u will use window.minsize then maxsize and resizable

'Screen attributes'
# both code will get width and height of ur monitor window
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

"Window attributes"
window.attributes('-alpha', 0.9) # to make window transparent
window.attributes('-topmost', True) # window will be on top of other window
#window.attributes('-fullscreen', True)
#window.overrideredirect(True) # to hide title bar of window
''' if u code window.overrideredirect(True) then u can't resize window so if u
    want to resize window then u have to add additional code, below '''
resizing = ttk.Sizegrip(window) #i am the below code
resizing.place(relx=1.0, rely=1.0, anchor='se')# i am the below code

label = ttk.Label(text='hello',foreground='darkcyan',)
label.pack()
window.mainloop()
