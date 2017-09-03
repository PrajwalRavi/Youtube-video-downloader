from collections import __main__
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import requests
from bs4 import BeautifulSoup

class GetByName:

    def __init__(self,name, location):

        self.res=[]
        self.name= name
        self.dow_loc= location
        self.vid_url= None
        self.master= Tk()
        self.opt = IntVar()
        self.vids = []
        self.urls = []

    def get_vids(self):

        master = self.master
        url = "https://www.youtube.com/results?search_query=" + self.name
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        a = soup.find_all("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ")

        for v in a:
            self.vids.append(v["title"])
            self.urls.append("https://www.youtube.com"+v["href"])

        i=0
        for v in self.vids:
            Radiobutton(master, text=v, variable=self.opt, value=i).grid(row=i, sticky=W)
            i+=1
        Button(text="OKAY", command=lambda: self.get_res(i,master)).grid(row=i)
        master.mainloop()

    def get_res(self, r, master):
        master.destroy()
        self.vid_url= self.urls[self.opt.get()]
        print(self.vid_url)


def main():

    obj= GetByName("lean on", "/")
    obj.get_vids()

if __name__=="__main__":
    main()

