import os
import sys
from tkinter import *
from tkinter import ttk
from p_gen_widgets import header_frame, generator_frame

# TODO: Add Manager page
# TODO: Add Database
# TODO: Login
# TODO: Register new user
# TODO: run -> pyinstaller --onefile main.spec

def img_resource_path(relative_path):
    """Source: https://github.com/Jtonna/Processes-Killer/blob/master/Process%20Killer/app/process_killer_app.py"""
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Styles
        self.style = ttk.Style()
        self.style.configure(style='Header.TFrame', background='#91b5c2')
        self.style.configure('TNotebook', background='#31294c')
        self.style.configure(style='TNotebook.Tab', background='#e0eaf3')
        self.style.configure(style='Generator.TFrame', background='#e0eaf3')

        # Header
        self.frame_header = header_frame.HeaderFrame(self, img_resource_path)
        self.frame_header.configure(borderwidth=1, relief='ridge', padding=5, style='Header.TFrame')
        self.frame_header.pack()

        # Main content -> Notebook
        self.tabbed_container = ttk.Notebook(self)
        self.tabbed_container.configure(padding=[0, 10, 0, 0])

        # Main content -> Generator
        self.password_generator = generator_frame.PasswordGenerator(self.tabbed_container)
        self.password_generator.configure(style='Generator.TFrame', padding=(5, 5, 15, 0))
        self.tabbed_container.add(self.password_generator, text='Generator')
        self.tabbed_container.pack()


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('GPasswords')
        self.geometry('490x335')
        self.resizable(False, False)
        self.iconphoto(True, PhotoImage(file=img_resource_path("img/icon_lock.png")))
        self.main_frame = MainFrame(self)
        self.main_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
