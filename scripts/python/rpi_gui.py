# GUI for 320x240 2.8 inch Raspberry Pi touch screen
# Features:
# - "Update" button: pulls from GitHub
# - Scrolling menu of lighting configurations

from tkinter import Tk, Frame, Label, Button
from tkinter import LEFT, RIGHT, TOP, BOTTOM, X, Y, BOTH

class RaveGUI(Tk):

    width_px = 320
    height_px = 240

    def __init__(self):
        root = Tk()
        root.title('Rave Controller')
        root.geometry('{}x{}'.format(self.width_px, self.height_px))
        root.resizable(width=False, height=False)

        root.focus_set()
        root.bind("<Escape>", quit)

        if root.winfo_screenwidth() == self.width_px and root.winfo_screenheight() == self.height_px:
            root.attributes('-fullscreen', True)

        # Frames
        left_frame = Frame(root)
        left_frame.pack(side=LEFT, fill=Y)

        righttop_frame = Frame(root, height=28)
        righttop_frame.pack(side=TOP, fill=X)

        rightbottom_frame = Frame(root)
        rightbottom_frame.pack(fill=BOTH, expand=1)

        # Objects
        exit_btn = Button(left_frame, text='Exit', command=quit)
        exit_btn.pack(side=TOP, fill=X)

        update_btn = Button(left_frame, text='Update')
        update_btn.pack(fill=BOTH, expand=1)

        prev_btn = Button(righttop_frame, text='<<')
        prev_btn.pack(side=LEFT)

        next_btn = Button(righttop_frame, text='>>')
        next_btn.pack(side=RIGHT)

        name_lbl = Label(righttop_frame, text='Rave Controller')
        name_lbl.place(relx=0.5, rely=0.5, anchor='c')

        # Start loop
        root.mainloop()

    def quit(self, e):
        e.widget.quit()


app = RaveGUI()
