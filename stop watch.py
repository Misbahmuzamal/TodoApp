import tkinter as tk
from time import strftime
root=tk.Tk()
root.title("Stop Watch")
def stop_watch():
    display_time= strftime("%H:%M:%S %p\n%m/%d/%Y")
    label.config(text=display_time)
    label.after(1000,stop_watch)

label=tk.Label(root,font=("calibri",50,"bold"),bg="yellow",fg="black")
label.pack(anchor="center")
stop_watch()
root.mainloop()


