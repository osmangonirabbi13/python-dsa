my_set = {1,2,3,4}
print(my_set)
print(type(my_set))

##add

s2 = set()

s2.add(1)
s2.add(2)
s2.add(3)
s2.add(5)
s2.add(6)
print(s2)

##remove 

s2.discard(1)
print(s2)

### FrozenSet : immutable set

fs = frozenset([1,2,3])
print(fs)
print(type(fs))