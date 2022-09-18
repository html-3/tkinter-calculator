
from tkinter import *
from tkinter import ttk


class View(Frame):
  PAD = 20
  BUTTON_CAPTIONS = [
    'C', '+/-', '%', '/',
    '7',  '8' , '9', '*',
    '4',  '5' , '6', '-',
    '1',  '2' , '3', '+',
    '0',  '.' , '='
    ]

  def __init__(self, app, controller) -> None:
    super().__init__()
    
    # Corresponding controller for this module
    self.controller = controller

    # Configuration and initialization functions
    self._config()
    self._make_display()
    self._make_buttons()

  def _config(self):
    # Frame customization
    self.pack(padx=self.PAD, pady=self.PAD)

  def _make_display(self):
    # Display initialization
    self.display = StringVar()
    ent = ttk.Entry(self, textvariable=self.display, state='disabled', justify='right')
    ent.pack(fill='x')

  def _make_buttons(self):
    # Buttons initialization
    
    frm = ttk.Frame(self)
    frm.pack()

    for i in range(0,5):
      for j in range(0,4):

        # Last row is shorter
        if j == 3 and i == 4:
          break

        caption = self.BUTTON_CAPTIONS[4*i+j]
        
        btn = ttk.Button(frm, text=caption, command=lambda button=caption: self.controller.callback(button))
        btn.grid(column=j, row=i, ipadx=10, sticky='ew', columnspan=2 if caption == '=' else 1)

