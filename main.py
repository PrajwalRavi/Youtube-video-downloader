from pytube import YouTube
from tkinter import *
from tkinter import ttk
from gi.repository import Notify
import re

import ytdownloader
import name
import url

def main():

    root1=Tk()
    gui_obj=ytdownloader.Gui(root1)
    gui_obj.get_mode()
    root1.mainloop()

    if gui_obj.mode.get()=="Name":

        obj = name.GetByName(gui_obj.vid.get(), gui_obj.dow_loc)
        obj.get_vids()
        download(obj)

    else:

        obj = url.GetByUrl(gui_obj.vid.get(), gui_obj.dow_loc)
        obj.get_res()
        download(obj)



def download(obj):

    root = Tk()
    root.title("Downloading :)")
    pb = ttk.Progressbar(root, orient='horizontal', length=300, mode='indeterminate')
    pb.pack()
    pb.start()
    yt = YouTube(obj.vid_url)
    format = re.search("\(\S+\)" , obj.res.get()).group()
    format = format[2:-1]
    resolution= re.search("-\s\S+p" , obj.res.get()).group()
    resolution= resolution[2:]
    video = yt.get(format, resolution)
    video.download(obj.dow_loc.get())
    pb.stop()
    show_noti(yt.filename)
    root.mainloop()

def show_noti(filename):

    Notify.init("Notification")
    summary = "Download Complete"
    body= filename+" has finished downloading :)"
    Notify.Notification.new(summary,body).show()


if __name__=="__main__":

    main()


