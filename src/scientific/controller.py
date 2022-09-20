
from src.scientific.model import Model
from src.scientific.view import View


class ScientificController:
  def __init__(self, app) -> None:
    self.model = Model()
    self.view = View(app, self)

  def callback(self, caption):
     result = self.model.calculate(caption)

     self.view.display.set(result)

  # NOT WORKING
  # Widget size and position
  def dimensions(self):
    return self.view.winfo_geometry()
