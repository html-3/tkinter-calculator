
from curses.ascii import isdigit


class Model:
  def __init__(self) -> None:

    self.previous = ''
    self.value = ''
    self.operator = ''

  def calculate(self, caption : str):
    if caption == 'C':
      self.value = ''
    
    elif caption.isdigit():
      self.value += caption

    elif caption == '+/-':
      self.value = self.value[1:] if '-' in self.value else '-' + self.value

    elif caption == '.' and not '.' in self.value:
      self.value += caption

    elif caption == '%':
      self.value = eval(f'{self.value}*100')

    elif caption == '=':
      self.value = self._evaluate()

    elif caption in ['+', '-', '/', '*']:
      if self.value:
        self.previous = self.value
        self.operator = caption
        self.value = ''

    return self.value

  def _evaluate(self):
    result = round(eval(self.previous + self.operator + self.value),3)
    return str(result)

