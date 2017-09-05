from pytube import YouTube
from tkinter import *
from tkinter import ttk
from gi.repository import Notify
import re
import threading
import os
import time

import ytdownloader
import name
import url


class DownloadThread(threading.Thread):
    def __init__(self, url, loc, res, format):
        threading.Thread.__init__(self)
        self.url = url
        self.res = res
        self.loc = loc
        self.format = format

    def run(self):
        yt = YouTube(self.url)
        video = yt.get(self.format, self.res)
        video.download(self.loc)
        show_noti(yt.filename)
        time.sleep(1)
        os._exit(0)


def main():
    root1 = Tk()
    gui_obj = ytdownloader.Gui(root1)
    gui_obj.get_mode()
    root1.mainloop()

    if gui_obj.mode.get() == "Name":

        obj = name.GetByName(gui_obj.vid.get(), gui_obj.dow_loc)
        obj.get_vids()
        download(obj)

    else:

        obj = url.GetByUrl(gui_obj.vid.get(), gui_obj.dow_loc)
        obj.get_res()
        download(obj)


def download(obj):
    format = re.search("\(\S+\)", obj.res.get()).group()
    format = format[2:-1]
    resolution = re.search("-\s\S+p", obj.res.get()).group()
    resolution = resolution[2:]

    download_thread = DownloadThread(obj.vid_url, obj.dow_loc.get(), resolution, format)
    download_thread.start()

    root = Tk()
    root.title("Downloading :)")
    pb = ttk.Progressbar(root, orient='horizontal', length=300, mode='indeterminate')
    pb.pack()
    pb.start()
    root.mainloop()


def show_noti(filename):
    Notify.init("Notification")
    summary = "Download Complete"
    body = filename + " has finished downloading. :)"
    Notify.Notification.new(summary, body).show()


if __name__ == "__main__":
    main()
