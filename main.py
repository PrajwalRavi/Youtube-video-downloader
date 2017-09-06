from tkinter import *
from tkinter import ttk
from gi.repository import Notify
import re
import threading
import os
import time

from pytube import YouTube

import ytdownloader
import name
import url


class DownloadThread(threading.Thread):
    """Class that defines the thread that downloads the video in the background.
    The class object takes the video resolution, format and download location as parmeters for the constructor.
    """

    def __init__(self, url, loc, res, format):
        """Initializes the instance variables of the object and initializes the __init__() method of Thread class."""

        threading.Thread.__init__(self)
        self.url = url
        self.res = res
        self.loc = loc
        self.format = format

    def run(self):
        """Starting point of the thread.
        This method that overrides the run() method in Thread class.
        """

        yt = YouTube(self.url)
        video = yt.get(self.format, self.res)
        video.download(self.loc)
        show_noti(yt.filename)
        time.sleep(0.5)
        os._exit(0)


def main():
    """Starting point of the program.

    First creates a window to get users choice on searching video based on URL or name and accepts URL/name and download
    location. This is done by creating an object of class Gui in ytdownloader module.

    Then, it creates another object of class GetByName or GetByUrl, based on user's choice. It then accepts resolution
     and format. After this, the video download begins ny invoking download() function.
    """

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
    """Extracts the resolution and format of the specified video.

    The thread download_thread is started so that the download can continue in the background.
    Meanwhile, the main thread displays the progress bar created using tkinter.ttk until the video download is complete.
    """

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
    """Displays a desktop notification when video download is complete.
    Uses the Notify module in gi repository.
    """

    Notify.init("Notification")
    summary = "Download Complete"
    body = filename + " has finished downloading. :)"
    Notify.Notification.new(summary, body).show()


if __name__ == "__main__":

    main()
