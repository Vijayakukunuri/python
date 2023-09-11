def charcount(s,v):
    count = 0
    for character in v:
        if character == s:
            count +=1
    return count
v= input("Enter a string: ")
s = input("Enter the character to be searched: ")
count = charcount(s,v)
print("Number of times character",v,"occurs in the string is:",count)



