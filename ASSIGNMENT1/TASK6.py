##Strings 
##counting number of vowels 
def swap(index1 , index2,string):
    string1 = list(string)
    temp = string1[index1]
    string1[index1]= string1[index2]
    string1[index2]=temp
    return ''.join(string1)

string = "Hallelujah"
count = 0
vowel = "AEIOUaeiou"
for alphabet in string:
    if alphabet in vowel:
        count += 1

print("no. of vowels = ",count)

##Reversing a string 
string1 = string
length = len(string)
i=0
while i<length/2 :
    string1 = swap(i,length-1-i,string1)
    i += 1
    

print(string1)
if string1 == string:
   print("yes string is a palindrome")
else :
    print("not a palindrome")



