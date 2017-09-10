from tkinter import *
from tkinter import ttk
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import time



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
        self.master = Tk()
        self.vid_url = None
        self.vid_urls = []
        self.playlists = []
        self.pl_urls = []
        self.pl_url = None

    def get_vids(self):
        """Scrapes the YouTube search results(based in user's query), extracts the video names from them and stores them
        in a list. It is then displayed to the user in a window in the form of radio-buttons.
        self.opt stores the user selected option.

        This method uses the Radiobutton method of Tk class to create the radio buttons.
        Scraping is done using BeautifulSoup
        """
        master=Tk()
        #master = Toplevel(root)
        #master.withdraw()
        #master.title("Choose one")
        url = "https://www.youtube.com/results?search_query=" + self.name
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        a = soup.find_all("h3", class_="yt-lockup-title ")
        vids=[]

        for v in a:
            nam = v.get_text()
            if (nam.find("Duration") > -1):
                vids.append(nam)
                self.vid_urls.append("https://www.youtube.com" + v.a["href"])
            else:
                self.playlists.append(nam[:-11])
                self.pl_urls.append("https://www.youtube.com" + v.a["href"])

        n = ttk.Notebook(master)
        n.grid(row=0, columnspan=20, rowspan=20)
        f1 = ttk.Frame(n)  # first page, which would get widgets gridded into it
        f2 = ttk.Frame(n)  # second page
        n.add(f1, text='Videos')
        n.add(f2, text='Playlists')

        self.opt1 = IntVar(master)
        self.opt2 = IntVar(master)

        #video:-
        l = Label(f1, text="Choose one of the following:", font=("Times", "20", "italic"))
        l.grid(row=0)
        i = 1  # i :- row number
        for v in vids:
            Radiobutton(f1, text=v, variable=self.opt1, value=i).grid(row=i, sticky=W)
            i += 1
        b = Button(f1, text="OKAY", command=lambda: self.get_res(master), font=("Times", "20", "bold italic"))
        b.grid(row=i)

        #playlist:-
        l = Label(f2, text="Choose one of the following:", font=("Times", "20", "italic"))
        l.grid(row=0)
        i = 1  # i :- row number
        for v in self.playlists:
            Radiobutton(f2, text=v, variable=self.opt2, value=i).grid(row=i, sticky=W)
            i += 1
        b = Button(f2, text="OKAY", command=lambda: self.get_playlist(master), font=("Times", "20", "bold italic"))
        b.grid(row=i)
        master.mainloop()

    def get_res(self, master):
        """Scrapes the YouTube search results(based in user's query), extracts the video URLs from them and stores them
        in a list. It is then displayed to the user in a window in the form of radio-buttons.

        This method again uses the Radiobutton method of Tk class to create the radio buttons.
        Scraping is done using BeautifulSoup
        """
        master.destroy()
        self.opt2.set(-1)
        self.vid_url = self.vid_urls[self.opt1.get() - 1]  # -1 because of 0-based indexing
        yt = YouTube(self.vid_url)
        resolutions = yt.get_videos()

        root = Tk()
        self.res = StringVar(root)
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

    def get_playlist(self,master):

        master.destroy()
        self.pl_url = self.pl_urls[self.opt2.get()-1]

