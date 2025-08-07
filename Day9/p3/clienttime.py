import sys

sys.path.append("C:/Users/H1646/PyCharm/PythonYT/SDET-QA/Day9/p1")
sys.path.append("C:/Users/H1646/PyCharm/PythonYT/SDET-QA/Day9/p2")

#approch1:
import testname
import testlang

testobj=testname.Test(1, 2)
testobj.testing()

learnobj=testlang.Learn(1, 2)
learnobj.learning()


#approch2:
from testname import *
testobj=Test(1, 2)
testobj.testing()

from testlang import *
learnobj=testlang.Learn(1, 2)
learnobj.learning()


