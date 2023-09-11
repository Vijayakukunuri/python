
def replaceVowel(string):
 newstr = ''
 for character in string:
     if character in 'aeiouAEIOU':
         newstr += '*'
     else:
         newstr += character
 return newstr
string = input("Enter a String: ")
string1 = replaceVowel(string)
print("The original String is:",string)
print("The modified String is:",string1)