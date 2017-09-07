from tkinter import *
from tkinter import filedialog


class Gui:
    """Creates the first window, to accept mode of search.

    Accepts the name/URL of the video.
    Can also set the download location. Default is the Downloads directory in Linux. Path differs for different OS.
    """

    def __init__(self, root):
        """Sets the instance variable dow_loc to default download location. Sets all other variables to None.

        master : tk object(main window).
        mode : mode of search
        vid : video name/URL
        """

        self.master = root
        self.dow_loc = StringVar()
        self.dow_loc.set("/home/prajwal/Downloads")     #This depends on your user name and Operating System
        self.mode = StringVar()

    def get_mode(self):
        """Defines all the widgets in the master window using the modules in tkinter package.
        """

        master = self.master
        master.title("Enter options")
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
        #The loc_disp label contains text that dynamically changes according to the chosen download location.
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
        """Creates the window for selecting download directory using filedialog module."""

        d = filedialog.askdirectory()
        self.dow_loc.set(d)


def main():
    """Creates the main GUI window when this module is run directly."""

    root1 = Tk()
    gui_obj = Gui(root1)
    gui_obj.get_mode()
    root1.mainloop()


if __name__ == "__main__":
    main()
