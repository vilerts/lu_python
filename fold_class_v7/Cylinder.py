import math

class Cylinder:

  def __init__(self, radius, height):
    self.radius = radius
    self.height = height

  def area (self):
    base_area = math.pi * (self.radius ** 2)
    side_area = 2 * math.pi * self.radius * self.height
    return side_area + 2 * base_area

  def volume(self):
      return math.pi * (self.radius ** 2) * self.height
