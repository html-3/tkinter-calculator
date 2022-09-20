from tkinter import *
from tkinter import ttk
import sv_ttk
from src.simple.controller import SimpleController
from src.scientific.controller import ScientificController


class App(Tk):
  def __init__(self) -> None:
    super().__init__()
    
    self._current = None
    self._swap_calc(ScientificController)

    self._menu()
    self._config()
    self._center_window()

  def run(self):  
    self.mainloop()

  def _config(self):
    self.title('MVCalc')
    sv_ttk.use_light_theme()
    self.configure(menu=self.menu_bar)

  def _center_window(self):

    self.update()
    w = self.winfo_width()
    h = self.winfo_height()

    x = (self.winfo_screenwidth() - w) // 2
    y = (self.winfo_screenheight() - h) // 2

    self.geometry(f'{w}x{h}+{x}+{y}')
    self.resizable(False, False)

  def _swap_calc(self, calc_obj):
    new = calc_obj(self)

    if self._current is not None:
      self._current.view.destroy()

    self._current = new
    print(self._current.dimensions())
    self._current.view.pack(pady=30, padx=30)

  def _menu(self):
    self.menu_bar = Menu(self)

    calc_type = Menu(self.menu_bar, tearoff=0)

    calc_type.add_command(label='Simple', command=lambda: self._swap_calc(SimpleController))
    calc_type.add_command(label='Scientific', command=lambda: self._swap_calc(ScientificController))

    self.menu_bar.add_cascade(label='Type', menu=calc_type)

    self.menu_bar.add_cascade(label='Quit', command=self.destroy)

