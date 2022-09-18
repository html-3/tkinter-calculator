from tkinter import *
from tkinter import ttk
import sv_ttk
from src.simple.controller import Controller


class App(Tk):
  def __init__(self) -> None:
    super().__init__()
    
    self.simple = Controller(self)
    self._config()
    self._center_window()

  def run(self):
    self.current = self.simple.view
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
