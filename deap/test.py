import operator
import random

from gp import PrimitiveSet, genFull, PrimitiveTree

tst_dict = {"add":1,"sub":5}
#print(tst_dict.keys())
#print(tst_dict.values())
pset = PrimitiveSet("main", 2)
pset.addPrimitive(operator.sub, 2, weight=0.5)
pset.addTerminal(2,weight=0.2)
pset.addTerminal(1,weight=0.5)
pset.addTerminal(3,weight=0.8)
pset.renameArguments(ARG0="x", weight=0.5)
pset.renameArguments(ARG1="y", weight=0.3)

# print("Before")
# for i in pset.terminals[object]:
#      print(i)
#      print(i.name,i.value,i.weight)

#TODO: implement random.choices for python 2.7? (only in 3.6 available)

weights = [i.weight for i in pset.terminals[object]]
print(weights)
# expr = genFull(pset,min_=1,max_=2)
# tree = PrimitiveTree(expr)
# print(tree)


#pset.addPrimitive(operator.add, 2)
#pset.addPrimitive(operator.mul, 2)