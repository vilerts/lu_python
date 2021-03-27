class Money:

  def __init__(self, euro):
    self.euro = euro

  def usd(self):
    return self.euro * 1.2

  def rub(self):
    return self.euro * 91.22
  
  def gbp(self):
    return self.euro * 0.88
  
  def pln(self):
    return self.euro * 4.48


class Money2:

  rates = {
    "USD" : 1.2,
    "GBP" : 0.88,
    "RUB" : 91.22,
    "PLN" : 4.48
  }

  def __init__(self, euro):
    self.euro = euro

  def usd(self):
    return self.euro * self.rates["USD"]

  def rub(self):
    return self.euro * self.rates["RUB"]
  
  def gbp(self):
    return self.euro * self.rates["GBP"]
  
  def pln(self):
    return self.euro * self.rates["PLN"]
