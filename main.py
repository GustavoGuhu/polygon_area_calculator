# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


#rect = shape_calculator.Rectangle(7, 3)
#print(rect.get_area())
#rect.set_width(20)
#print(rect.get_perimeter())
#print(rect)
#rect.get_picture()
#print(rect.get_diagonal())
#print(rect.get_amount_inside(shape_calculator.Rectangle(2,1)))

#sq = shape_calculator.Square(2)
#print(sq.get_area())
#sq.set_side(4)
#print(sq.get_diagonal())
#print(sq)
#sq.set_side(3)
#print(sq.get_picture())



# Run unit tests automatically
main(module='test_module', exit=False)