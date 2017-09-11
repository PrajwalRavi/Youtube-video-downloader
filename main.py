import os
import re
import time
import multiprocessing
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import requests
from bs4 import BeautifulSoup
from gi.repository import Notify
from pytube import YouTube

import url
import name
import ytdownloader


def start():

    root = Tk()
    img = PhotoImage(file="logo.gif")
    l = Label(root, image=img, height= 200)
    st = Button(root , text="Start new download", font=("Times", "25", "bold", "italic")  , command = lambda : main(root))
    cancel = Button(root , text="Cancel", font=("Times", "25", "bold", "italic")  , command = lambda : sys.exit(0))
    l.pack()
    st.pack()
    cancel.pack()
    root.mainloop()


def main(master):
    """Starting point of the program.

    First creates a window to get users choice on searching video based on URL or name and accepts URL/name and download
    location. This is done by creating an object of class Gui in ytdownloader module.

    Then, it creates another object of class GetByName or GetByUrl, based on user's choice. It then accepts resolution
     and format. After this, the video download begins ny invoking download() function.
    """

    master.destroy()
    root1 = Tk()
    gui_obj = ytdownloader.Gui(root1)
    gui_obj.get_mode()
    root1.mainloop()

    if gui_obj.mode.get() == "Name":

        obj = name.GetByName(gui_obj.vid.get(), gui_obj.dow_loc.get())
        obj.get_vids()

        #pb_bar = multiprocessing.Process(target=p_bar)
        #pb_bar.start()

        if obj.opt2.get() == -1:
            download(obj)

        else:
            r = requests.get(obj.pl_url)
            soup = BeautifulSoup(r.content, "lxml")
            v = soup.find_all("li", class_="yt-uix-scroller-scroll-unit  vve-check")
            for vid in v:
                print(vid["data-video-id"])
                url = "https://www.youtube.com/watch?v=" + vid["data-video-id"]
                down_onebyone(url, gui_obj.dow_loc.get())

        #pb_bar.terminate()
        #start()

    else:
        obj = url.GetByUrl(gui_obj.vid.get(), gui_obj.dow_loc)
        obj.get_res()
        download(obj)

def p_bar():

    title = "Downloading"
    root = Tk()
    root.title(title)
    pb = ttk.Progressbar(root, orient='horizontal', length=300, mode='indeterminate')
    pb.grid(row=0)
    pb.start()  # starts the progress bar
    Button(root, text="Cancel", command=lambda: os._exit(0)).grid(row=1)
    root.mainloop()

def down_onebyone(url, dow_loc):
    """Downloads the videos in the playlist one by one in mp4, 360p format.

    :param url: URL of video to be downloaded in the playlist
    :param dow_loc: Download location
    :return: None
    """

    yt = YouTube(url)
    video = yt.get("mp4", "360p")  # format can be changed as needed
    try:
        video.download(dow_loc)
        show_noti(yt.filename)
        time.sleep(0.5)  # required so that program does not exit before displaying the desktop notification.

    except OSError:
        messagebox.showerror("Error", "1 Video already present in the folder.")


def download(obj):
    """Extracts the resolution and format of the specified video.

    The thread download_thread is started so that the download can continue in the background.
    Meanwhile, the main thread displays the progress bar created using tkinter.ttk until the video download is complete.
    """

    format = re.search("\(\S+\)", obj.res.get()).group()  # uses regular expressions
    format = format[2:-1]
    resolution = re.search("-\s\S+p", obj.res.get()).group()  # uses regular expressions
    resolution = resolution[2:]

    pb_bar = multiprocessing.Process(target=p_bar)
    pb_bar.start()

    yt = YouTube(obj.vid_url)
    video = yt.get(format, resolution)
    try:
        video.download(obj.dow_loc)
        show_noti(yt.filename)
        time.sleep(0.1)  # required so that program does not exit before displaying the desktop notification.
        pb_bar.terminate()
        #start()  # starts the whole program again.

    except OSError:
        messagebox.showerror("Error", "Video already present in the folder.")
        os._exit(0)

def show_noti(filename):
    """Displays a desktop notification when video download is complete.

    Uses the Notify module in gi repository.
    """

    Notify.init("Notification")
    summary = "Download Complete"
    body = filename + " has finished downloading. :)"
    Notify.Notification.new(summary, body).show()


if __name__ == "__main__":
    start()
