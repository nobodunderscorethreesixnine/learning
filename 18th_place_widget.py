import tkinter as tk

window = tk.Tk()
window.title('Place')
window.geometry('400x600')

label1 = tk.Label(window, text='label1', background='red')
label2 = tk.Label(window, text='label2', background='blue')
label3 = tk.Label(window, text='label3', background='green')
button1 = tk.Button(window, text='button')

#layout
label1.place(x=100,y=100, width=200, height=50)
# placing layout by using realtive method (relx=0.0 to 0.9 and rely=0.0 to 0.9)
label2.place(relx=0.0, rely=0.0,width=300, height=40, anchor='nw')#or we can use
#relwidth and relheight to make responsive instead of widht and height.
#if we define widget with relwidth and relheight, it's height and width
#change respective of its window
label3.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.2)

button1.place(relx=1, rely=1, anchor='se')

frame = tk.Frame(window)
frame_label = tk.Label(frame, text='Frame label', background = 'yellow')
frame_button = tk.Button(frame, text='Frame button')

frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=0.2, relheight=0.5)
frame_button.place(relx=0.1, rely=0.0,relwidth=0.5, relheight=0.5,
                   )

##exercise of place

window = tk.Tk()
window.title('place exercise')
window.geometry('600x600')

exercise_label = tk.Label(window, text='label', background='black')
exercise_label.place(relx=0.5, rely=0.5,height=200,
            anchor='center',relwidth=0.5)
# we can combine both relwidth and height or relheight and width it works well
#with each other.If width is relative(relwidth) then width is responsive
#and height is not ,viceversa


window.mainloop()

