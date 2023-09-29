import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.title('treeview or table')
##window.geometry('400x400')

first_names = ['bob','maria', 'alex', 'james']
last_names = ['Smith', 'Brown', 'Wilson', 'Cook']

#treeview - creating table 
table = ttk.Treeview(window,columns=('first','last','email'),show='headings')
#show='headings' push first heading to left side as default show is blank like
#show='',inorder to push first heading to left we have to show='headings'

table.heading('first',text='Frist Name')
table.heading('last',text='Last Name')
table.heading('email',text='Email')

table.pack(fill='both',expand=True)

# inserting value inside table with .insert()
table.insert(parent='',index=0, values= ('birat','gautam','biratg@gmail.com'))

for i in range(51):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@gmail.com'
    data = (first , last , email)

    table.insert(parent='',index=0 , #index change position in table
                 values = data) #values=(first, last, email)

#tk.END means sometimes we don't where is end so using tk.END put value in end
table.insert(parent='', index=tk.END,values=('xxxx','yyy','zzz'))

# events
def item_select(_):
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)




#here event param dont't work so we have to consider another options
table.bind('<<TreeviewSelect>>',item_select)
table.bind('<Delete>',delete_items)


window.mainloop()

