setA={1,2,3,4,5,6,7}
print("setA IS",setA)
setB={3,4,9,10,12,22}
print("setB IS",setB)
unionset=setA.union(setB)
print("union of sets is",unionset)
print ("length of union set is",len(unionset))
removedset=unionset.remove(22)
print("removed itm in union set is",unionset)
print ("length of union set is",len(unionset))