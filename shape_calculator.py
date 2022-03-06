class Rectangle:

  def __init__(self, w, h):
    self.w = w
    self.h = h

  def __str__(self):
    return ("Rectangle(width=%d, height=%d)" % (self.w, self.h))

  def set_width(self, w):
    self.w = w

  def set_height(self, h):
    self.h = h
  
  def get_area(self):
    self.area = self.w*self.h
    return self.area
  
  def get_perimeter(self):
    self.perimeter = 2 * self.w + 2 * self.h
    return self.perimeter

  def get_diagonal(self):
    self.diag = (self.w ** 2 + self.h ** 2) ** .5
    return self.diag

  def get_picture(self):
    if (self.h > 50 or self.w > 50):
      return ("Too big for picture.")
    else:
      draw = ""
      for i in range(0, self.h):
        draw += (self.w*("*")+"\n")
      return draw
  
  def get_amount_inside(self, o_shape):
    ow = o_shape.w
    oh = o_shape.h
    qw = int(self.w/ow)
    qh = int(self.h/oh)
    return qh*qw
    

class Square(Rectangle):
  
  def __init__(self, s):
    self.w = s
    self.h = s
    self.s = s

  def __str__(self):
    return ("Square(side=%d)" % (self.s))

  def set_width(self, s):
    self.w = s
    self.h = s
    self.s = s

  def set_height(self, s):
    self.w = s
    self.h = s
    self.s = s

  def set_side(self, s):
    self.w = s
    self.h = s
    self.s = s