from tkinter import *
from tkinter import ttk


class ResultsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Geometry -> Columns
        for i in range(7):
            self.columnconfigure(i, minsize=66)
        # Result
        ttk.Label(self, text='  Your secure password: ', background='#e0eaf3'). \
            grid(column=0, columnspan=2, row=0, sticky='w')
        self.password = StringVar(value='')
        self.password_output = ttk.Entry(self,
                                         state="readonly",
                                         textvariable=self.password,
                                         font=('Consolas', 11),
                                         width=21)
        self.password_output.grid(column=2, columnspan=3, row=0, sticky='w')
        # Copy & Save
        self.btn_copy_password = ttk.Button(self, text='Copy', width=7, command=self.copy_to_clipboard)
        self.btn_copy_password.grid(column=5, row=0)

        self.btn_save_password = ttk.Button(self, text='Save', width=7, state=DISABLED)
        self.btn_save_password.grid(column=6, row=0)

    def clear_form(self):
        self.password.set('')

    def set_password(self, password: str):
        self.password.set(password)

    def copy_to_clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.password.get())
        r.destroy()
