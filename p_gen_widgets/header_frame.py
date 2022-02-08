from tkinter import *
from tkinter import ttk


class HeaderFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.logo = PhotoImage(file='img/logo.png')
        # Column definitions
        self.columnconfigure(0, minsize=70)
        self.columnconfigure(1, minsize=240)
        self.columnconfigure(2, minsize=90)
        self.columnconfigure(3, minsize=90)
        # Widgets
        ttk.Label(self, image=self.logo, background='#91b5c2').grid(row=0, column=0, sticky='w')
        ttk.Label(self, text='GPasswords', background='#91b5c2', font=('Bahnschrift', 18)). \
            grid(row=0, column=1, sticky='w')
        ttk.Button(self, text='Log in').grid(row=0, column=2, sticky='w', pady=(30, 0))
        ttk.Button(self, text='New user').grid(row=0, column=3, sticky='w', pady=(30, 0))
