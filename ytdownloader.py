from tkinter import *
from tkinter import filedialog


class Gui:
    def __init__(self, root):
        self.master = root
        self.dow_loc = StringVar()
        self.dow_loc.set("/home/prajwal/Downloads")
        self.mode = StringVar()
        self.vid = None

    def get_mode(self):
        master = self.master
        self.vid = StringVar()
        option_list = ("Name", "URL")
        self.mode.set("Name")

        label1 = Label(master, text="Search by: ", font=("Times", "24", "italic"))
        option = OptionMenu(master, self.mode, *option_list)
        okay = Button(master, text="Okay", command=master.destroy, font=("Times", "20", "bold italic"))
        label2 = Label(master, text="Download location:", font=("Times", "24", "italic"))
        label3 = Label(master, text="Video name / URL: ", font=("Times", "24", "italic"))
        tex_input = Entry(master, textvariable=self.vid, font=("Times", "20"))
        self.loc_disp = Label(master, bg="white", textvariable=self.dow_loc, padx=20, font=("Helvetica", "20"))
        browse = Button(master, text="Browse", command=self.get_loc, font=("Times", "20", "italic"))

        option.grid(row=0, column=1, sticky="W")
        label1.grid(row=0, column=0, sticky=E)
        label2.grid(row=1, column=0)
        browse.grid(row=1, column=2)
        label3.grid(row=2)
        self.loc_disp.grid(row=1, column=1)
        tex_input.grid(row=2, column=1, sticky=W)
        okay.grid(columnspan=3)

    def get_loc(self):
        d = filedialog.askdirectory()
        self.dow_loc.set(d)


def main():
    root1 = Tk()
    gui_obj = Gui(root1)
    gui_obj.get_mode()
    root1.mainloop()


if __name__ == "__main__":
    main()
