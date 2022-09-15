
from tkinter import *
from tkinter import ttk
import sv_ttk

class View(Tk):
  PAD = 20
  MAX_COL = 4
  BUTTON_CAPTIONS = [
    'C', '+/-', '%', '/',
    '7',  '8' , '9', '*',
    '4',  '5' , '6', '-',
    '1',  '2' , '3', '+',
    '0',  '.' , '='
    ]

  def __init__(self, controller) -> None:
    super().__init__()

    self.controller = controller
    self.title('MVCalc')
    self.value_var = StringVar()
    sv_ttk.use_light_theme()

    self._make_frame()
    #self.withdraw()
    self._make_entry()
    self._make_buttons()
    self._center_window()

  def run(self):
    self.mainloop()

  def _make_frame(self):
    self.frm = ttk.Frame(self)
    self.frm.pack(padx=self.PAD, pady=self.PAD)

  def _make_entry(self):
    ent = ttk.Entry(self.frm, textvariable=self.value_var, state='disabled', justify='right')
    ent.pack(fill='x')

  def _make_buttons(self):
    frm = ttk.Frame(self.frm)
    frm.pack()

    for i in range(0,5):
      for j in range(0,4):

        if j == 3 and i == 4:
          break

        caption = self.BUTTON_CAPTIONS[4*i+j]

        btn = ttk.Button(frm, text=caption, command=lambda button=caption: self.controller.callback(button))
        btn.grid(column=j, row=i, ipadx=10, sticky='ew', columnspan=2 if caption == '=' else 1)

  def _center_window(self):

    self.update()
    w = self.winfo_width()
    h = self.winfo_height()

    x = (self.winfo_screenwidth() - w) // 2
    y = (self.winfo_screenheight() - h) // 2

    self.geometry(f'{w}x{h}+{x}+{y}')
    self.resizable(False, False)