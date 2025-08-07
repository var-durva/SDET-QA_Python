#first import predefine module as client module is not part of pack1
import sys #sys is the predefine module
sys.path.append("C:/Users/H1646/PyCharm/PythonYT/SDET-QA/Day9/Pack1")

#approch 1
import module1
import module2

module1.display()
module2.show()

#approch 2:
from module1 import *
from module2 import *

display()
show()