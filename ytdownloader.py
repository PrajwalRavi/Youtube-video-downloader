from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import re


class Gui:

	def __init__(self,root):

		master=root
		option_list = ("Name", "URL")
		selection = StringVar()
		selection.set("Name")

		label1= Label(text="Search by:")
		option=OptionMenu(master, selection, *option_list)
		okay = Button(text="Okay")
		label2 = Label(text="Download location:")
		browse= Button(text="Browse", command=self.get_loc)

		option.grid(row=0, column=1)
		label1.grid(row=0, column=0, sticky=E)
		label2.grid(row=1, column=0)
		browse.grid(row=1, column=1)
		okay.grid(columnspan=2)

	def get_loc(self):

		self.dow_loc = filedialog.askdirectory()
		print(self.dow_loc)














root=Tk()
gui_obj = Gui(root)


root.mainloop()