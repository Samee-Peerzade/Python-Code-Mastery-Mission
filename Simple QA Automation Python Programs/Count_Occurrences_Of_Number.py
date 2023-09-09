# Count the Number of element in the list:

#How many times the number has occur

mylist=[15,6,7,10,5,10,4,3,10,15,10]
x=10
count=0

for ele in mylist:
    if(ele==x):
        count=count+1
        
print("{} has occured {} times".format(x,count))

#Approach-2 using count()
mylist=[15,6,7,10,5,10,4,3,10,15,10]
x=15
print("{} has occured {} times".format(x,mylist.count(x)))










