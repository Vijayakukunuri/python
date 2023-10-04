#classes and obj
#objects
#__init__ is initializer:
class furniture():
    chairs=5
    tables=6
    racks=6

   # def __init__(self,chairs,tables,racks):
        ##self.chairs=chairs
       # self.tables=tables
        #self.racks=racks

    def __init__(self ,chairs,tables,racks=8):
        self.chairs=chairs
        self.tables=tables
        self.racks=racks
f2obj=furniture(9,8)

print(f2obj.chairs,f2obj.tables,f2obj.racks)

#fobj=furniture(7,9,8)

#print(fobj.chairs,fobj.tables,fobj.racks)

#classes constructors

class workerdata():
    worker="surya"
    id=87655
    salary=6000
    industry="Hindustan pvy.lim"
    def __workerdata__(self,worker,id,salary,industry):
        self.worker=worker
        self.id=id
        self.salary=salary
        self.industry=industry
class subsec(workerdata):
    dresscode="uniform"
    times=9
    def __init__(self,dresscode,times):

        self.dresscode=dresscode
        self.times=times


obj=workerdata()
print(obj.worker,obj.id,obj.salary,obj.industry)

obj1=subsec("civil",8)
print(obj1.worker,obj1.id,obj1.salary,obj1.industry,obj1.dresscode,obj1.times)








