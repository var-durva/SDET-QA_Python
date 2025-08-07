import sys
sys.path.append("C:/Users/H1646/PyCharm/PythonYT/SDET-QA/Day9/package1")
sys.path.append("C:/Users/H1646/PyCharm/PythonYT/SDET-QA/Day9/package1/package2")
#approch 1
import module1
import module2
module1.display()
module2.show()

#approch 2
from module1 import *
display()
from module2 import *
show()

