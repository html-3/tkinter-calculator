
from src.simple.model import Model
from src.simple.view import View


class Controller:
  def __init__(self, app) -> None:
    self.model = Model()
    self.view = View(app, self)

  def callback(self, caption):
     result = self.model.calculate(caption)

     self.view.display.set(result)
