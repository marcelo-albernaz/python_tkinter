from tkinter import *

win= Tk ()

win.title("janela")
win.geometry("150x80")


lb= Label(win,text=" codando em py")
lb.pack()
bt= Button(win,text="clica ai",background="blue",activebackground="#00008B",command=win.destroy)
bt.pack()





win.mainloop()