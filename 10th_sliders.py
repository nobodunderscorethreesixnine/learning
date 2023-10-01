import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext# it is not widget it is like ttk. This has contents
#of a widget

window = tk.Tk()
window.title('Sliders')
window.geometry('400x400')

#slider
scale_float= tk.DoubleVar(value=15) #invar only store int so in this case we have to
#use another variable doublevar but acc to situation we can use intvar also
##scale_int = tk.Intvar(value=15)

scale = ttk.Scale(window, command =lambda value:progress.stop(), from_ =0,
                  to=25, length=300, orient='vertical',variable=scale_float)
scale.pack()

#progress bar
progress = ttk.Progressbar(window,variable=scale_float,maximum=25,
                           orient='horizontal',mode='determinate',#indetermine=default
                           length=400)
progress.pack()
#preogress methods
progress.start(1000)# 1000=it change progress bar in every 1 seconds
#above start()method will change variable of other related widget also in this
#case it will change value of variable of scale_float and those related widgets
##progress.stop()


#Scroll text
scrooltext = scrolledtext.ScrolledText(window, width=50)#this is not one widget 
#it is mixture of text and slider widget . we can make it ourselve
scrooltext.pack()




window.mainloop()

