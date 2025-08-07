#accessiong/call function from one module to another module
#Approch 1:
import calculator
calculator.add(12,3)
calculator.multi(12, 2)

#Approch 2:
from calculator import add,multi
add(12,3)
multi(12, 2)

#Approch 3:
from calculator import *            #* is representing all function and classes.
add(12,3)
multi(12, 2)