from tkinter import *
from tkinter import messagebox, ttk, filedialog

window = Tk()
window.title('Words Counter')
window.resizable(0,0)

title = Label(window, text='Live Word Counter', font=('Times New Roman', 24, 'bold'))
title.pack()

frame = Frame(window)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

notepad = Text(frame, yscrollcommand=scrollbar.set, font=('Times New Roman', 12), width=100)
notepad.pack(padx=5,pady=5,side=LEFT,fill=BOTH)

scrollbar.config(command=notepad.yview)

ftypes = [('Text Files', '*.txt'), ('Batch Files', '*.bat'), 
              ('HTML Files', '*.html')]

def count(event):
    text = notepad.get(1.0, END)
    text_lst = text.split()
    length = len(text_lst)
    label.config(text='WORD COUNT: '+str(length))
    
def imp():
    global ftypes
    fd = filedialog.askopenfile(filetypes=ftypes)
    location = fd.name
    try:
        myfile = open(location, 'r')
        imp_text = myfile.read()
        notepad.delete(1.0, END)
        notepad.insert(1.0, imp_text)
        count(event=None)
    except Exception as e:
        messagebox.showerror('ERROR', e)

def save():
    global ftypes
    fd = filedialog.asksaveasfile()
    location = fd.name
    text = notepad.get(1.0, END)
    try:
        myfile = open(location, 'w')
        myfile.write(text)
        myfile.close()
        messagebox.showinfo('INFORMATION', 'SAVED SUCCESSFULLY')
    except Exception as e:
        messagebox.showerror('ERROR', e)
    
    
    
    
label = Label(window, text='WORD COUNT: 0', font=('Consolas', 11, 'bold'))
label.pack(pady=5,padx=5)

window.bind('<space>', count)
window.bind('<BackSpace>', count)
window.bind('<Return>', count)
window.bind('<Delete>', count)
window.bind('<Control-Key-z>', count)
window.bind('<Control-Key-y>', count)
window.bind('<Control-Key-v>', count)

btn1 = ttk.Button(window, text='IMPORT TEXT', width=20, command=imp)
btn1.pack(pady=5)

btn2 = ttk.Button(window, text='SAVE TEXT', width=20, command=save)
btn2.pack(pady=5)

window.mainloop()
