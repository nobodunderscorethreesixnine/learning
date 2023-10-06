import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('frame and parenting')
window.geometry('400x400')

#frame
frame = ttk.Frame(window,width=100, height=200,borderwidth=5,
                  relief=tk.GROOVE)#relief=tk.FLAT,RIDGE,RAISED,SUNKEN,GROOVE
frame.pack_propagate(False)#can be written frame.propogate(False) also,
# if false then parents width and height are respedcted
#else child width and height will be respected
frame.pack(side='left')

label = ttk.Label(frame,text='hello i am inside frame widget')

label.pack()

button = ttk.Button(frame,text='click_me',command=lambda:print('inside frame'))
button.pack()

label = ttk.Label(window,text='outside of window')
label.pack(side='left')

#one liner
exercise_frame = ttk.Frame(window)
ttk.Label(exercise_frame,text='another widget').pack()
ttk.Button(exercise_frame , text='button').pack()
tk.Entry(exercise_frame).pack(side='left')

exercise_frame.pack(side='right')#always try to pack after putting other widget
# inside the frame don't forget

window.mainloop()
