from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import re

class youtube:
	""" Simple script to download youtube videos providing GUI functionality.
	
	This program uses the modules: tkinter, pytube, requests, re and BeautifulSoup.
	It accepts the name of the youtube video ans the exact download location.
	Functionality to specify resolution download location using GUI will be added in upcoming versions.
	"""
	
	def __init__(self):
		"Specfies the object attributes."
		self.search=""
		self.dow_loc=""
		
	def get_par(self,s,d,root):
		"Destroys the initial input window and assigns the object attribute the inputs."
		root.withdraw()
		#root=Tk()
		messagebox.showinfo("Downloading...." , "Downloading....\nYou will get a message once its complete.")
		self.search=s
		self.dow_loc=d
		self.download()
		#root.mainloop()
	
	def download(self):
		"""Downloads the specific video.
		
		This module scrapes the search results from Youtube search using requests module and obtains the URL of 
		the first search result. This is then used to download the video by passing it to YouTube module of pytube package.
		A message is displayed after the download is complete.
		"""
			
		print("PATIENCE IS A VIRTUE :)")
		url="https://www.youtube.com/results?search_query="+self.search
		r=requests.get(url)
		soup=BeautifulSoup(r.content, "lxml")
		a=soup.find("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link ")
		vid_id=a["href"]
		url="https://www.youtube.com"+vid_id
		yt=YouTube(url)
		#formats=[(re.search("\(\S+\)",str(s)).group())[1:-1] for s in yt.get_videos()]
		#res=[(re.search(
		video= yt.get("mp4", "360p")		
		video.download(self.dow_loc)
		messagebox.showinfo("Done" , "Download complete!!")
		sys.exit()
	
	def gui(self):
		"Displays the initial window to  accept input from the user using tkinter module."
		root = Tk()
		v1=StringVar()
		v2=StringVar()				
		se_label=Label(root, text="SEARCH: ")
		se_entry=Entry(root, textvariable=v1)
		loc_label=Label(root, text="DOWLOAD LOCATION: ")
		loc_entry=Entry(root, textvariable=v2)
		d_but=Button(root, text="Download", command= lambda: self.get_par(v1.get(), v2.get(),root))
		se_label.grid(row=0, sticky=E)
		se_entry.grid(row=0, column=1)
		loc_label.grid(row=1)
		loc_entry.grid(row=1, column=1)
		d_but.grid(columnspan=2)
		root.mainloop()
		
		
	def main(self):
		"Beginning of the program."
		self.gui()
	
if(__name__=="__main__"):
	obj=youtube()
	obj.main()

	
	
	
