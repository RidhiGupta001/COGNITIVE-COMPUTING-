##Data Structures 

##list 
list1 = [5,10,15,20,25,30,35,40,45]

##using inbuilt function
a = min(list1)
print("smallest in the list = ",a)
##using loop
i = list1[0]
for val in list1:
    if val < i:
        i = val
print("smallest in the list = ",i)

##Dictionaries

capitals1 = {"India" : "NewDelhi",
            "China": "Beijing",
            "Australia":"Canberra",
            }
print("Capital of Australia = ", capitals1.get("Australia"))

##Sorting Numbers 

##Ascending 
list1.sort()
print(list1)

##Descending
list1.sort(reverse = True)
print(list1)

##Merging 2 dictionaries 
capitals2 = {"Japan": "Tokyo",
             "Bhutan": "Thimphu"}
capitals3 = capitals1 | capitals2
print(capitals3)


