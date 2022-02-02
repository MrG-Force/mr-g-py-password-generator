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
        self.password_generator.configure(style='Generator.TFrame', padding=(5, 5, 15, 0))
        self.tabbed_container.add(self.password_generator, text='Generator')
        self.tabbed_container.pack()


class PasswordGenerator(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Styles
        self.style = ttk.Style()
        self.style.configure('TLabelframe', background='#e0eaf3')
        self.style.configure('TLabelframe.Label', background='#e0eaf3')
        self.style.configure('TRadiobutton', background='#e0eaf3')
        self.style.configure('TSpinbox', background='#e0eaf3')
        self.style.configure('TFrame', background='#e0eaf3')

        # Geometry -> Columns
        for i in range(7):
            self.columnconfigure(i, minsize=70)

        # Geometry -> Rows
        for i in range(4):
            self.rowconfigure(i, minsize=55)

        # Instance variables
        self.pass_len = IntVar(value=9)
        self.pass_type = StringVar(value='Random')

        # Password length selector
        ttk.Label(self, text='Password length: ', background='#e0eaf3').grid(column=0, row=0, columnspan=2, sticky='e')
        self.len_select = ttk.Spinbox(self,
                                      from_=9, to=128,
                                      textvariable=self.pass_len,
                                      width=7,
                                      state='readonly')
        self.len_select.grid(column=2, row=0)

        # Type of password selector
        self.frame_pass_type = ttk.LabelFrame(self, text='Password type  ')
        self.frame_pass_type.grid(column=3, columnspan=4, row=0)
        self.p_types = ('Random', 'Custom')
        grid_column = 0
        for t in self.p_types:
            radio = ttk.Radiobutton(self.frame_pass_type,
                                    text=t,
                                    value=t,
                                    variable=self.pass_type,
                                    command=lambda: self.toggle_password_type())
            radio.grid(column=grid_column, row=0, ipadx=15, ipady=5)
            grid_column += 1

        # Define letters, numbers, symbols
        self.inputs_chars = HowManyCharsSelector(self, self.pass_len)
        self.inputs_chars.configure(padding=[0, 10, 10, 15], text='How many...  ')
        self.inputs_chars.grid(column=0, columnspan=7, row=1, sticky='w')

        # Action buttons
        self.btn_gen_password = ttk.Button(self, text='Generate')
        self.btn_gen_password.grid(column=2, row=2)

        self.btn_gen_password = ttk.Button(self, text='Reset', command=self.reset_form)
        self.btn_gen_password.grid(column=4, row=2)

        # Results
        self.output_password = ResultsFrame(self)
        self.output_password.configure(borderwidth=1, relief='groove', padding=(5, 10, 10, 10))
        self.output_password.grid(column=0, columnspan=7, sticky='nw')

    def toggle_password_type(self):
        if self.pass_type.get() == 'Random':
            self.inputs_chars.set_selectors_state('disabled')
            self.inputs_chars.clear_form()
            self.pass_len.set(9)
            self.len_select.configure(state='readonly')
        else:
            self.inputs_chars.set_selectors_state('readonly')
            self.pass_len.set(0)
            self.len_select.configure(state='disabled')

    def reset_form(self):
        self.pass_len.set(9)
        self.pass_type.set('Random')
        self.toggle_password_type()
        self.output_password.clear_form()


class ResultsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Geometry -> Columns
        for i in range(7):
            self.columnconfigure(i, minsize=66)
        # Result
        ttk.Label(self, text='  Your secure password: ', background='#e0eaf3'). \
            grid(column=0, columnspan=2, row=0, sticky='w')
        self.password = StringVar(value='34@#r%56p{$rF00O')
        self.password_output = ttk.Entry(self,
                                         state="readonly",
                                         textvariable=self.password,
                                         font=('Cascadia Code Light', 11),
                                         width=21)
        self.password_output.grid(column=2, columnspan=3, row=0, sticky='w')
        # Copy & Save
        self.btn_copy_password = ttk.Button(self, text='Copy', width=7)
        self.btn_copy_password.grid(column=5, row=0)

        self.btn_save_password = ttk.Button(self, text='Save', width=7, state=DISABLED)
        self.btn_save_password.grid(column=6, row=0)

    def clear_form(self):
        self.password.set('')


class HowManyCharsSelector(ttk.LabelFrame):
    def __init__(self, container, pass_len: IntVar):
        super().__init__(container)
        # Geometry -> Columns
        for i in range(6):
            self.columnconfigure(i, minsize=77)
        # Variables
        self.max_length = 128
        self.avail_chars = self.max_length
        self.inputs = [IntVar(value=0) for i in range(3)]
        self.label_names = ['Letters: ', 'Numbers: ', 'Symbols: ']
        self.state = 'disabled'

        # Labels
        column = 0
        for i in range(3):
            ttk.Label(self, text=self.label_names[i], background='#e0eaf3').grid(column=column, row=0, sticky='e')
            column += 2

        # Selectors
        self.sel_letters = ttk.Spinbox(self,
                                       from_=0, to=self.avail_chars,
                                       textvariable=self.inputs[0],
                                       width=5,
                                       state=self.state,
                                       command=lambda: self.update_password_length(pass_len)
                                       )
        self.sel_letters.bind('<<Increment>>', lambda e: self.decrease_range(e, 0))
        self.sel_letters.bind('<<Decrement>>', lambda e: self.increase_range(e, 0))

        self.sel_numbers = ttk.Spinbox(self,
                                       from_=0, to=self.avail_chars,
                                       textvariable=self.inputs[1],
                                       width=5,
                                       state=self.state,
                                       command=lambda: self.update_password_length(pass_len)
                                       )
        self.sel_numbers.bind('<<Increment>>', lambda e: self.decrease_range(e, 1))
        self.sel_numbers.bind('<<Decrement>>', lambda e: self.increase_range(e, 1))

        self.sel_symbols = ttk.Spinbox(self,
                                       from_=0, to=self.avail_chars,
                                       textvariable=self.inputs[2],
                                       width=5,
                                       state=self.state,
                                       command=lambda: self.update_password_length(pass_len)
                                       )
        self.sel_symbols.bind('<<Increment>>', lambda e: self.decrease_range(e, 2))
        self.sel_symbols.bind('<<Decrement>>', lambda e: self.increase_range(e, 2))

        self.sel_letters.grid(column=1, row=0, sticky='w')
        self.sel_numbers.grid(column=3, row=0, sticky='w')
        self.sel_symbols.grid(column=5, row=0, sticky='w')

        self.selectors = [self.sel_letters, self.sel_numbers, self.sel_symbols]

    def decrease_range(self, event, index):
        if self.avail_chars > 0:
            self.avail_chars -= 1
            # print(f'Available chars: {self.avail_chars}\n')  # DEBUG
            for i in range(3):
                if i != index:
                    self.selectors[i].configure(to=self.inputs[i].get() + self.avail_chars)

    def increase_range(self, event, index):
        if self.avail_chars < self.max_length:
            self.avail_chars += 1
            # print(f'Available chars: {self.avail_chars}\n')  # DEBUG
            for i in range(3):
                if i != index:
                    self.selectors[i].configure(to=self.inputs[i].get() + self.avail_chars)

    def get_input_values(self):
        return self.inputs

    def set_selectors_state(self, state):
        self.state = state
        for selector in self.selectors:
            selector.configure(state=self.state)

    def clear_form(self):
        self.avail_chars = self.max_length
        for i in self.inputs:
            i.set(0)

    def update_password_length(self, length: IntVar):
        length.set(self.max_length - self.avail_chars)


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
        self.geometry('490x335')
        self.resizable(False, False)

        self.iconphoto(True, PhotoImage(file='icon_lock.png'))

        self.main_frame = MainFrame(self)
        self.main_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
