#approch 1
import animal, birds

animal.fly()
animal.color()

birds.fly()
birds.color()

#approch 2: Same functions in 2 modules
from animal import *
fly()
color()

from birds import *
fly()
color()