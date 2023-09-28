import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('canvas')
window.geometry('400x400')

canvas = tk.Canvas(window,bg='darkcyan')
canvas.pack()

###line
##canvas.create_line((20,50,20,150),width=10,fill='black' ) #x1,y1,x2,y2
##
###rectangle
##canvas.create_rectangle((80,50,150,150),#left,top,right,bottom
##                        fill='black',width=5,outline='darkred')
###oval
##canvas.create_oval((150,0,50,50),fill='red')
##
###polygon
##canvas.create_polygon((100,100,100,200,300,50),fill='pink')
##
###arc
##canvas.create_arc((200,0,300,100),fill='black',start=45,extent=180,
##                  style=tk.ARC,outline='red',width=10)
#text
canvas.create_text((150,150),text='hello world',fill='red',width=200)

#to create widget inside canvas
canvas.create_window((100,100),
                     window=ttk.Label(window,text='this is inside canvas widget',
                     ))


#exercise
window = tk.Tk()
window.title('paint')
window.geometry('400x400')

canvas = tk.Canvas(window,bg='darkcyan')
canvas.pack()

def draw_on_canvas(event):
   x = event.x
   y = event.y
   canvas.create_oval((x-brush_size / 2 , y-brush_size /2, x+brush_size/2,
                       y+brush_size/2),
                      fill='black',)
def brush_size_adjust(event):
   global brush_size
   if event.delta > 0:
      brush_size += 4
   else:
      brush_size -= 4

   brush_size = max(0,min(brush_size,50))

brush_size = 4

canvas.bind('<Motion>',draw_on_canvas)
canvas.bind('<MouseWheel>',brush_size_adjust)

window.mainloop()

