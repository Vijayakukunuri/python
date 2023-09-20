#using write
cf=open("C:\\Users\\Lenovo\\Desktop\\vijju\\createfile1.txt","w+")
cf.write("welcome to my file world :")

#using w+
#cf=open("C:\\Users\\Lenovo\\Desktop\\vijju\\createfile1.txt","w+")
cf.write("trip")

#using writelines
list1=["fruits","veggies","s@i"]
for items in list1:
    cf.writelines(items)



