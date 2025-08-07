#Approch 1:
import a, b

aobj= a.Animal()
aobj.display()

bobj= b.Bird()
bobj.display()


#Approch 2:
from a import Animal
from b import Bird
aobj1=Animal()
aobj1.display()
bobj1=Bird()
bobj1.display()
