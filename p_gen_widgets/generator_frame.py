from tkinter import *
from tkinter import ttk
import generator
import num_chars_sel_frame as char_select


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

        # Password type selector
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
        self.inputs_chars = char_select.NumberOfCharsSelector(self, self.pass_len)
        self.inputs_chars.configure(padding=[0, 10, 10, 15], text='How many...  ')
        self.inputs_chars.grid(column=0, columnspan=7, row=1, sticky='w')

        # Action buttons
        self.btn_gen_password = ttk.Button(self, text='Generate', command=self.generate_password)
        self.btn_gen_password.grid(column=2, row=2)

        self.btn_gen_password = ttk.Button(self, text='Reset', command=self.reset_form)
        self.btn_gen_password.grid(column=4, row=2)

        # Results
        self.output_password = ResultsFrame(self)
        self.output_password.configure(borderwidth=1, relief='groove', padding=(5, 10, 10, 10))
        self.output_password.grid(column=0, columnspan=7, sticky='nw')

    def generate_password(self):
        inputs = self.inputs_chars.get_input_values()
        p = generator.generate(inputs[0], inputs[1], inputs[2], self.pass_len.get())
        self.output_password.set_password(p)

    def toggle_password_type(self):
        if self.pass_type.get() == 'Random':
            self.inputs_chars.set_selectors_state('disabled')
            self.inputs_chars.clear_form()
            self.output_password.clear_form()
            self.pass_len.set(9)
            self.len_select.configure(state='readonly')
        else:
            self.inputs_chars.set_selectors_state('readonly')
            self.pass_len.set(0)
            self.output_password.clear_form()
            self.len_select.configure(state='disabled')

    def reset_form(self):
        self.pass_len.set(9)
        self.pass_type.set('Random')
        self.toggle_password_type()
        self.output_password.clear_form()