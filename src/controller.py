
from src.model import Model
from src.view import View


class Controller:
  def __init__(self) -> None:
    self.model = Model()
    self.view = View(self)

  def callback(self, caption):
     result = self.model.calculate(caption)

     self.view.value_var.set(result)

  def run(self):
    self.view.run()