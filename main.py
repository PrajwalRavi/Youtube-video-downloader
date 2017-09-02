import ytdownloader
import name

root1=Tk()
gui_obj=ytdownloader.Gui(root1)
gui_obj.get_mode()
root1.mainloop()

if gui_obj.mode=="Name":

    root = Tk()
    obj = name.GetByName(root,gui_obj.vid.get(), gui_obj.dow_loc)
    obj.get_vids()
    root.mainloop()
