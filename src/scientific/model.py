
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

    elif not self.value:
      pass
      
    elif caption == '+/-':
      self.value = self.value[1:] if '-' in self.value else '-' + self.value

    elif caption == '.' and not '.' in self.value:
      self.value += caption

    elif caption == '%':
      self.value = round(eval(f'{self.value}*100'),6)

    elif caption in ['+', '-', '/', '*']:
      if self.value:
        self.previous = self.value
        self.operator = caption
        self.value = ''

    elif caption == '=' and self.previous:
      self.value = self._evaluate()

    self.value = str(self.value)

    return self.value

  def _evaluate(self):
    result = round(eval(self.previous + self.operator + self.value),6)
    return str(result)

