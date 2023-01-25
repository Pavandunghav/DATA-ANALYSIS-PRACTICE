# numpy7

#filtering the arrays 

#filtering the array means if the value of particular element is true it will be shown in the filtered array 
# elements  with the false   value will get excluded 



#this is the one method where we assign values to the element and print the filterd array 
import numpy as np

a=np.array([2,3,4,545,6,1])

x=[True,False,False, True,False,True]

newa=a[x]

print(newa)


#filtering is done by creating the normal array of the true or false values and assign it to the original array 

#by using b=a[x]


x1=[]

for i in a:
    if i<10:
        x1.append(True)
    else:
        x1.append(False)
        
a2=a[x1]
print(a2)



#finally the shortest method of the filteration 

b=np.array([34,5,4,3,32,2])

f=b<10

newb=b[f]

print(f)
print(newb)



