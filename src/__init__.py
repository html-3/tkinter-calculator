from tkinter import *
from tkinter import ttk
import sv_ttk
from src.simple.controller import Controller


class App(Tk):
  def __init__(self) -> None:
    super().__init__()
    
    self.simple = Controller(self)
    self.scientific = Controller(self)

    self._menu()
    self._config()
    self._center_window()

  def run(self):
    self.current = self.simple.view
    self.mainloop()

  def _config(self):
    self.title('MVCalc')
    sv_ttk.use_light_theme()
    self.configure(menu=self.menu_bar)

    self.scientific.view.forget()


  def _center_window(self):

    self.update()
    w = self.winfo_width()
    h = self.winfo_height()

    x = (self.winfo_screenwidth() - w) // 2
    y = (self.winfo_screenheight() - h) // 2

    self.geometry(f'{w}x{h}+{x}+{y}')
    self.resizable(False, False)

  def _change_calculator(self, new : Frame):
    self.current.forget()
    self.current = new
    self.current.pack()

  def _menu(self):
    self.menu_bar = Menu(self)

    calc_type = Menu(self.menu_bar, tearoff=0)

    calc_type.add_command(label='Simple', command=lambda: self._change_calculator(self.simple.view))
    calc_type.add_command(label='Scientific', command=lambda: self._change_calculator(self.scientific.view))

    self.menu_bar.add_cascade(label='Type', menu=calc_type)

    self.menu_bar.add_cascade(label='Quit', command=self.destroy)

