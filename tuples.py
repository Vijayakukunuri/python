mytuple = ("apple", "banana", "cherry", "apple", "guava")
print(mytuple)
#length of tuple
print("length is",len(mytuple))
#revere of a tuple
def Reverse1(mytuple):
    new_tup = mytuple[::-1]
    print("reverse is",(new_tup))
Reverse1(mytuple)
#slicing
print(type(mytuple))
print("slicing is",(mytuple[1:-1]))
#append
addtuple=list(mytuple)
addtuple.append("tuppas")
mytuple=tuple(addtuple)
print("append  tuple",addtuple)
thistuple = ("apple", "banana", "cherry")
#using while loop
i=0
while i < len(mytuple):
    print("objects in the mytuple =",mytuple[i])
    i+=1
tuple1 = ("a","b","c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("combing two tuples=",tuple3)
productuple=mytuple*3
print(productuple)

