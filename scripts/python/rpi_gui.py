import os
import math

from subprocess import Popen, call
from tkinter import Tk, Frame, Label, Button
from tkinter import LEFT, RIGHT, TOP, X, Y, BOTH


class RaveGUI(Tk):

    width_px = 320
    height_px = 240
    light_btn_width = 14
    light_btn_height = 4
    ignored_files = ['__pycache__', 'README.md', 'opc.py', 'opc.pyc', 'fastopc.py', 'opcutil.py',
                     'rpi_gui.py', 'test.py', 'color-correction-ui.py', 'usb-lowlevel.py',
                     'firmware-config-ui.py', 'opcutil.pyc']
    current_page = 0
    all_files = os.listdir('.')
    lighting = None

    def __init__(self):
        super().__init__()
        for name in self.ignored_files:
            try:
                self.all_files.remove(name)
            except ValueError:
                pass

        root = Tk()
        root.title('Rave Controller')
        root.geometry('{}x{}'.format(self.width_px, self.height_px))
        root.resizable(width=False, height=False)

        root.focus_set()
        root.bind("<Escape>", self.quit)

        if root.winfo_screenwidth() == self.width_px and root.winfo_screenheight() == self.height_px:
            root.attributes('-fullscreen', True)

        # Frames
        left_frame = Frame(root)
        left_frame.pack(side=LEFT, fill=Y)

        righttop_frame = Frame(root, height=28)
        righttop_frame.pack(side=TOP, fill=X)

        self.rightbottom_frame = Frame(root)
        self.rightbottom_frame.pack(fill=BOTH, expand=1)

        # Objects
        exit_btn = Button(left_frame, text='Exit', command=self.quit)
        exit_btn.pack(side=TOP, fill=X)

        update_btn = Button(left_frame, text='Update', command=self.update)
        update_btn.pack(fill=BOTH, expand=1)

        prev_btn = Button(righttop_frame, text='<<', command=self.next_page)
        prev_btn.pack(side=LEFT)

        next_btn = Button(righttop_frame, text='>>', command=self.prev_page)
        next_btn.pack(side=RIGHT)

        name_lbl = Label(righttop_frame, text='Rave Controller')
        name_lbl.place(relx=0.5, rely=0.5, anchor='c')

        # Initialize light buttons
        self.init_light_btns(self.current_page)

        # Start loop
        root.mainloop()

    def init_light_btns(self, page):
        # Get files for current page
        files = self.all_files[6 * page: 6 * (page + 1)]
        files += [''] * (6 - len(files))

        light1_btn = Button(self.rightbottom_frame,
                            width=self.light_btn_width,
                            height=self.light_btn_height,
                            text=files[0],
                            command=self.config_function(files[0]))
        light1_btn.grid(row=0, column=0)

        light2_btn = Button(self.rightbottom_frame,
                            width=self.light_btn_width,
                            height=self.light_btn_height,
                            text=files[1],
                            command=self.config_function(files[1]))
        light2_btn.grid(row=0, column=1)

        light3_btn = Button(self.rightbottom_frame,
                            width=self.light_btn_width,
                            height=self.light_btn_height,
                            text=files[2],
                            command=self.config_function(files[2]))
        light3_btn.grid(row=1, column=0)

        light4_btn = Button(self.rightbottom_frame,
                            width=self.light_btn_width,
                            height=self.light_btn_height,
                            text=files[3],
                            command=self.config_function(files[3]))
        light4_btn.grid(row=1, column=1)

        light5_btn = Button(self.rightbottom_frame,
                            width=self.light_btn_width,
                            height=self.light_btn_height,
                            text=files[4],
                            command=self.config_function(files[4]))
        light5_btn.grid(row=2, column=0)

        light6_btn = Button(self.rightbottom_frame,
                            width=self.light_btn_width,
                            height=self.light_btn_height,
                            text=files[5],
                            command=self.config_function(files[5]))
        light6_btn.grid(row=2, column=1)

    def config_function(self, fn):
        def set_config():
            if self.lighting:
                self.lighting.terminate()
            self.lighting = Popen(['python', fn])
        return set_config

    def next_page(self):
        self.current_page = (self.current_page + 1) % (math.ceil(len(self.all_files) / 6))
        self.init_light_btns(self.current_page)

    def prev_page(self):
        self.current_page = (self.current_page - 1) % (math.ceil(len(self.all_files) / 6))
        self.init_light_btns(self.current_page)

    def update(self):
        print('updating')
        call(['git', 'pull'])
        self.init_light_btns(self.current_page)

    def quit(self):
        self.lighting.terminate()
        exit()


app = RaveGUI()
