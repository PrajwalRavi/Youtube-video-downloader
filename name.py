from tkinter import *
from pytube import YouTube
import requests
from bs4 import BeautifulSoup

class GetByName:

    def __init__(self,name, location):


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

        l=Label(master, text = "Choose one of the following:", font= ("Times", "20", "italic"))
        i=1
        for v in self.vids:
            Radiobutton(master, text=v, variable=self.opt, value=i).grid(row=i, sticky=W)
            i+=1

        l.grid(row=0)
        b = Button(text="OKAY", command=lambda: self.get_res(master), font= ("Times", "20", "bold italic"))
        b.grid(row=i)
        master.mainloop()


    def get_res(self, master):

        master.destroy()
        self.vid_url= self.urls[self.opt.get()]
        yt=YouTube(self.vid_url)
        resolutions=yt.get_videos()

        root=Tk()
        self.res = StringVar()
        l=Label(root, text="Choose resolution:", font= ("Times", "20", "italic"))
        b=Button(root, text="Download", command = lambda : root.destroy(), font= ("Times", "20", "bold italic"))

        r_num=1
        for r in resolutions:
            but=Radiobutton(root, text=r, variable=self.res, value=r)
            but.grid(row=r_num, sticky=W)
            r_num+=1

        l.grid(row=0)
        b.grid(row=r_num)
        root.mainloop()



def main():

    obj= GetByName("lean on", "/")
    obj.get_vids()
    obj.get_res()

if __name__=="__main__":
    main()

