from collections import __main__
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import requests
from bs4 import BeautifulSoup


class Gui:

	def __init__(self,root):

		self.master=root
		self.dow_loc=StringVar()
		self.dow_loc.set("/home/prajwal/Desktop/Downloads")

	def get_method(self):

		master=self.master
		option_list = ("Name", "URL")
		selection = StringVar()
		selection.set("Name")

		label1 = Label(master, text="Search by:")
		option = OptionMenu(master, selection, *option_list)
		okay = Button(master, text="Okay", command=master.destroy)
		label2 = Label(master, text="Download location:")
		self.loc_disp= Label(master, bg="white", textvariable=self.dow_loc)
		browse = Button(master, text="Browse", command=self.get_loc)

		option.grid(row=0, column=1, sticky="W")
		label1.grid(row=0, column=0, sticky=E)
		label2.grid(row=1, column=0)
		browse.grid(row=1, column=2)
		self.loc_disp.grid(row=1, column=1)
		okay.grid(columnspan=3)


	def get_loc(self):

		d = filedialog.askdirectory()
		self.dow_loc.set(d)

	def get_info(self,root):

		master=root















def main_root_def():

	root1=Tk()
	gui_obj = Gui(root1)
	gui_obj.get_method()
	root1.mainloop()

	root2=Tk()
	gui_obj.get_info(root2)

	root2.mainloop()





if __name__=="__main__":
	main_root_def()
