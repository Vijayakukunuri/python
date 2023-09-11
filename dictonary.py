car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
y= car.values()
print(x) #before the change
print(y)
car["color"] = "white"
print(x)
print(y)#after the change