# GUI for 320x240 2.8 inch Raspberry Pi touch screen
# Features:
# - "Update" button: pulls from GitHub
# - Scrolling menu of lighting configurations

import tkinter as tk

class RaveGUI(tk.Tk):

    width_px = 320
    height_px = 240

    def __init__(self):
        root = tk.Tk()
        root.title('Rave Controller')
        root.geometry('{}x{}'.format(self.width_px, self.height_px))
        root.resizable(width=False, height=False)

        root.focus_set()
        root.bind("<Escape>", lambda e: e.widget.quit())

        if root.winfo_screenwidth() == self.width_px and root.winfo_screenheight() == self-height_px:
            root.attributes('-fullscreen', True)

        # Frames
        left_frame = tk.Frame(root)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        righttop_frame = tk.Frame(root, height=28)
        righttop_frame.pack(side=tk.TOP, fill=tk.X)

        rightbottom_frame = tk.Frame(root)
        rightbottom_frame.pack(fill=tk.BOTH, expand=1)

        # Objects
        exit_btn = tk.Button(left_frame, text='Exit')
        exit_btn.pack(side=tk.TOP, fill=tk.X)

        update_btn = tk.Button(left_frame, text='Update')
        update_btn.pack(fill=tk.BOTH, expand=1)

        prev_btn = tk.Button(righttop_frame, text='<<')
        prev_btn.pack(side=tk.LEFT)

        next_btn = tk.Button(righttop_frame, text='>>')
        next_btn.pack(side=tk.RIGHT)

        name_lbl = tk.Label(righttop_frame, text='Rave Controller')
        name_lbl.place(relx=0.5, rely=0.5, anchor='c')

        # Start loop
        root.mainloop()


app = RaveGUI()
