from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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
        self.frame_header = FrameHeader(self)
        self.frame_header.configure(borderwidth=1, relief='ridge', padding=5, style='Header.TFrame')
        self.frame_header.pack()

        # Main content -> Notebook
        self.tabbed_container = ttk.Notebook(self)
        self.tabbed_container.configure(padding=[0, 10, 0, 0])
        # Main content -> Generator
        self.password_generator = PasswordGenerator(self.tabbed_container)
        self.password_generator.configure(style='Generator.TFrame')
        self.tabbed_container.add(self.password_generator, text='Generator')
        self.tabbed_container.pack()


class PasswordGenerator(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.style = ttk.Style()
        self.style.configure('TLabelframe', background='#e0eaf3')
        self.style.configure('TLabelframe.Label', background='#e0eaf3')
        self.style.configure('TRadiobutton', background='#e0eaf3')
        self.style.configure('TSpinbox', background='#e0eaf3')
        self.style.configure('TFrame', background='#e0eaf3')
        # Geometry -> Columns
        self.columnconfigure(0, minsize=70)
        self.columnconfigure(1, minsize=70)
        self.columnconfigure(2, minsize=70)
        self.columnconfigure(3, minsize=70)
        self.columnconfigure(4, minsize=70)
        self.columnconfigure(5, minsize=70)
        self.columnconfigure(6, minsize=70)
        # Geometry -> Rows
        self.rowconfigure(0, minsize=55)
        self.rowconfigure(1, minsize=35)
        self.rowconfigure(2, minsize=55)
        self.rowconfigure(3, minsize=55)
        self.rowconfigure(4, minsize=55)

        self.pass_len = StringVar(value=None)
        self.pass_type = StringVar(value='Random')

        # Password length selector
        ttk.Label(self, text='Password length: ', background='#e0eaf3').grid(column=0, row=0, columnspan=2, sticky='e')
        self.len_select = ttk.Spinbox(self,
                                      from_=9, to=128,
                                      textvariable=self.pass_len,
                                      width=7,
                                      wrap=True,
                                      state='readonly')
        self.len_select.grid(column=2, row=0)

        # Type of password selector
        self.frame_pass_type = ttk.LabelFrame(self, text='Password type  ')
        self.frame_pass_type.grid(column=3, columnspan=4, row=0)
        self.p_types = ('Random', 'Custom')
        grid_column = 0
        for t in self.p_types:
            radio = ttk.Radiobutton(self.frame_pass_type, text=t, value=t, variable=self.pass_type)
            radio.grid(column=grid_column, row=0, ipadx=15, ipady=5)
            grid_column += 1

        # Define letters, numbers, symbols
        self.num_char_inputs = FramePasswordChars(self)
        self.num_char_inputs.configure(padding=[0, 10, 30, 20], text='How many...  ')
        self.num_char_inputs.grid(column=0, columnspan=7, row=1, sticky='nw')


class FramePasswordChars(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, minsize=78)
        self.columnconfigure(1, minsize=78)
        self.columnconfigure(2, minsize=78)
        self.columnconfigure(3, minsize=78)
        self.columnconfigure(4, minsize=78)
        self.columnconfigure(5, minsize=78)

        self.letters = StringVar(value=None)
        self.numbers = StringVar(value=None)
        self.symbols = StringVar(value=None)
        self.max_length = 126
        self.char_types = ('Letters: ', 'Numbers: ', 'Symbols: ')
        self.char_vars = [self.letters, self.numbers, self.symbols]

        g_column = 0
        text_var = 0
        for t in self.char_types:
            ttk.Label(self, text=t, background='#e0eaf3').grid(column=g_column, row=0, sticky='e')
            g_column += 1
            selector = ttk.Spinbox(self, from_=1, to=self.max_length, textvariable=self.char_vars[text_var], width=5)
            text_var += 1
            selector.grid(column=g_column, row=0, sticky='w')
            g_column += 1


class FrameHeader(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.logo = PhotoImage(file='logo.png')
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


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('GPasswords')
        self.geometry('490x380')
        self.resizable(False, False)

        self.iconphoto(True, PhotoImage(file='icon_lock.png'))

        self.main_frame = MainFrame(self)
        self.main_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
