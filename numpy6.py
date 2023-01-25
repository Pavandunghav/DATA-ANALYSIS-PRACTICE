#searching in the array 

#searching is done by a funtcion where()
import numpy as np 

a=np.array([2,3,4,5,6,78,9,2])


x=np.where(a==6)
print(x)


print(np.where(a==2))


# to find the index of the even numbers in the array 

y=np.where(a%2==0)
print(y)


#here (in the parenthesis give arrayname%2 == 0)


#to find the odd elements at the indexes  use (where(a%2==1))

z=np.where(a%2==1)

print(z)


# there is a anpther function to search the place where a particular value should be inserted 
#by using the function searchsorted()

z1=np.searchsorted(a,8)

print(z1)


#sorting in the arrays 

#sorting in the arrays is done by the functon sort()


#this is the syntax bruh...
print(np.sort(a))



#sorting of the non numeric array 

ba=np.array(["a","z","b","c","d","e"])

print(np.sort(ba))

#it will sort it according the place in the alphabetical order 

ba2=np.array(["apple","zebra","bat","cow","deer","elephant"])

print(np.sort(ba2))

