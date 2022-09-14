

from src.controller import Controller

class App:
  def __init__(self) -> None:
    self.controller = Controller()

  def run(self):
    self.controller.view.run()