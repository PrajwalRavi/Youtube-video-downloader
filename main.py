import ytdownloader
import name
from tkinter import *

root1=Tk()
gui_obj=ytdownloader.Gui(root1)
gui_obj.get_mode()
root1.mainloop()
if gui_obj.mode.get()=="Name":

    obj = name.GetByName(gui_obj.vid.get(), gui_obj.dow_loc)
    obj.get_vids()
    print(obj.res.get())
