#example:
#Package   #modules #classes   #Methods
#p1 ===> testname => Test :  testing
#p2 ===> testlang => Learn  :  learning
#p 3 ===> clienttime

class Test:
    def __init__(self, test1, test2):
        self.test1 = test1
        self.test2 = test2
    def testing(self):
        print(self.test1, self.test2)

# testobj=Test(1, 2)
# testobj.testing()