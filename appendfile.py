#using "a"
cf=open("C:\\Users\\Lenovo\\Desktop\\vijju\\createfile1.txt","a")
cf.write(" newly added")

#using "a+"
cf=open("C:\\Users\\Lenovo\\Desktop\\vijju\\createfile1.txt","a+")
print(cf.write("\n lost the append"))
print(cf.read())

