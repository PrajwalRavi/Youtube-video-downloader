from tkinter import *
from pytube import YouTube
import requests
from bs4 import BeautifulSoup


class GetByUrl:

    def __init__(self,url, location):

        self.vid_url= url
        self.dow_loc= location
        self.res= None

    def get_res(self):

        yt=YouTube(self.vid_url)
        resolutions=yt.get_videos()

        root=Tk()
        self.res = StringVar()
        l=Label(root, text="Choose resolution:")
        b=Button(root, text="Download", command = lambda : root.destroy())

        r_num=1
        for r in resolutions:
            but=Radiobutton(root, text=r, variable=self.res, value=r)
            but.grid(row=r_num, sticky=W)
            r_num+=1

        l.grid(row=0)
        b.grid(row=r_num)
        root.mainloop()

def main():

    obj= GetByUrl("https://www.youtube.com/watch?v=kJQP7kiw5Fk" , "/")
    obj.get_res()

if __name__=="__main__":

    main()

