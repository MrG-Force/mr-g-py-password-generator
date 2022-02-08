from tkinter import *
from tkinter import ttk


class NumberOfCharsSelector(ttk.LabelFrame):
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
            for i in range(3):
                if i != index:
                    self.selectors[i].configure(to=self.inputs[i].get() + self.avail_chars)

    def get_input_values(self):
        return [i.get() for i in self.inputs]

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
