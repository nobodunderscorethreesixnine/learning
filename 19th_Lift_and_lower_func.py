##exercise of place

import tkinter as tk

window = tk.Tk()
window.title('place exercise')
window.geometry('600x600')

label1 = tk.Label(window, text='label1', background='green')
label2 = tk.Label(window, text='label2', background='red',
                  width=50)

button1 = tk.Button(window, text='raise label 1',
                    command=lambda:label1.lift(aboveThis = label2))
## there is argument for both lift and tkraise func 'aboveThis'.
## aboveThis simply tells specific widget to lift of other widget like in
## above code label1 is only able to lift above of label2 not label3.If we try
## to lift label1 above to label3 then it will not work because arguemtn is label2


' or in place of label1.life() u can use label1.tkraise()'
button2=tk.Button(window, text='raise label 2',command=lambda:label2.lift())

## we can use lift() to lift the widget from other widget like z-index in html
## we can use lower() to lower the widget from other widget.
'1 way to do this is'
##label1.lift()
##label2.lower()

label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)

## we can also give command to button

button1.place(rely=1, relx=0.8,anchor='se')
button2.place(rely=1, relx=1,anchor='se')

#exercise
label3 = tk.Label(window, text='label 3', background='yellow')
label3.place(x=200, y=150, width=190, height=100)

button3 = tk.Button(window, text='raise label 3', command=lambda:label3.tkraise())
button3.place(relx=.6, rely=1,anchor='se')

window.mainloop()
