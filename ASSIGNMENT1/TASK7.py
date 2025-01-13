##File Handling

##Reading
f = open('Mydata.txt','r')
print(f.read())

##Reading total no. of lines 
lines = len(f.readlines())
print("total no of lines = ",lines)


##Writing
f1 = open('Myfile.txt','a')
f1.write("Let's see if it's writing")
