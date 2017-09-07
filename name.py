from tkinter import *
from pytube import YouTube
import requests
from bs4 import BeautifulSoup


class GetByName:
    """This class is used when the user wishes to search a video by it's name.

    Attributes:-
        name: Video name as input by the user
        dow_loc: Download location selected by the user
        master: Tk object that defines the window containing all the widgets
        opt: Serial number of the video selected by the user from the list of options
        vids: List of all video names scraped from YouTube search results
        urls:  List of all corresponding video URLs scraped from YouTube search results
    """

    def __init__(self, name, location):
        """Initializes all the instance variables."""

        self.name = name
        self.dow_loc = location
        self.vid_url = None
        self.master = Tk()
        self.opt = IntVar()
        self.vids = []
        self.urls = []

    def get_vids(self):
        """Scrapes the YouTube search results(based in user's query), extracts the video names from them and stores them
        in a list. It is then displayed to the user in a window in the form of radio-buttons.
        self.opt stores the user selected option.

        This method uses the Radiobutton method of Tk class to create the radio buttons.
        Scraping is done using BeautifulSoup
        """

        master = self.master
        master.title("Select any one")
        url = "https://www.youtube.com/results?search_query=" + self.name
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        a = soup.find_all("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ")

        for v in a:
            self.vids.append(v["title"])
            self.urls.append("https://www.youtube.com" + v["href"])

        l = Label(master, text="Choose one of the following:", font=("Times", "20", "italic"))
        l.grid(row=0)
        i = 1   # i :- row number
        for v in self.vids:
            Radiobutton(master, text=v, variable=self.opt, value=i).grid(row=i, sticky=W)
            i += 1
        b = Button(text="OKAY", command=lambda: self.get_res(master), font=("Times", "20", "bold italic"))
        b.grid(row=i)
        master.mainloop()

    def get_res(self, master):
        """Scrapes the YouTube search results(based in user's query), extracts the video URLs from them and stores them
        in a list. It is then displayed to the user in a window in the form of radio-buttons.

        This method again uses the Radiobutton method of Tk class to create the radio buttons.
        Scraping is done using BeautifulSoup
        """

        master.destroy()
        self.vid_url = self.urls[self.opt.get() - 1]        # -1 because of 0-based indexing
        yt = YouTube(self.vid_url)
        resolutions = yt.get_videos()

        root = Tk()
        self.res = StringVar()
        l = Label(root, text="Choose resolution:", font=("Times", "20", "italic"))
        b = Button(root, text="Download", command=lambda: root.destroy(), font=("Times", "20", "bold italic"))

        r_num = 1
        for r in resolutions:
            but = Radiobutton(root, text=r, variable=self.res, value=r)
            but.grid(row=r_num, sticky=W)
            r_num += 1

        l.grid(row=0)
        b.grid(row=r_num)
        root.mainloop()


def main():
    """Starting poinnt of the program."""

    obj = GetByName("lean on", "/")
    obj.get_vids()
    obj.get_res()


if __name__ == "__main__":

    main()
