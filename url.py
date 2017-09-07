from tkinter import *
from pytube import YouTube


class GetByUrl:
    """This class is used when the user wishes to search a video by it's name.

    Attributes:-
        vid_url : Stores the video URL entered by the user
        res     : Video resolution selected by the user
        dow_loc : Video download location selected by the user
    """

    def __init__(self, url, location):
        """Initializes the instance variables."""

        self.vid_url = url
        self.dow_loc = location
        self.res = None

    def get_res(self):
        """Displays the list of available video resolutions to the user in a window.

        The selected option is stored in the res variable.
        """

        yt = YouTube(self.vid_url)
        resolutions = yt.get_videos()

        root = Tk()
        root.title("Select any one")
        self.res = StringVar()
        l = Label(root, text="Choose resolution:", font=("Times", "20", "italic"))
        b = Button(root, text="Download", command=lambda: root.destroy(), font=("Times", "20", "bold italic"))

        r_num = 1  # r_num : row number
        for r in resolutions:
            but = Radiobutton(root, text=r, variable=self.res, value=r)
            but.grid(row=r_num, sticky=W)
            r_num += 1

        l.grid(row=0)
        b.grid(row=r_num)
        root.mainloop()


def main():
    """Starting point of the program. """
    obj = GetByUrl("https://www.youtube.com/watch?v=kJQP7kiw5Fk", "/")
    obj.get_res()


if __name__ == "__main__":
    main()
