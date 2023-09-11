conset=set()
print(conset)
print("the no of elements are=",len(conset))
homogeneousSet={1,2,3,4,5,6,7,8}
print(homogeneousSet)
print("the no of elements are=",len(homogeneousSet))
hetrogeneousSet={1,2,3,4,5,"surya","kiran","nani","vijji"}
print(hetrogeneousSet)
print("the no of elements are=",len(hetrogeneousSet))
print("the datatype in hetrogeneousSet",type(set))
for x in hetrogeneousSet:
  print(x)
homogeneousSet.add("orange")
print("modified homogeneousset",homogeneousSet)
#add two sets
myset={"table","cooler","fan","bed"}
newset={"house","car","chair","pen"}
myset.update(newset)
print("updated set is",myset)
hetrogeneousSet.discard("nani")
print("the disgardes set", hetrogeneousSet)
#removed item in set
hetrogeneousSet.remove("vijji")
print("removed item in set",hetrogeneousSet)
#pop in set
popset = hetrogeneousSet.pop()
print("removed item in hetrogeneousset",popset)
print("the set after removal",hetrogeneousSet)




