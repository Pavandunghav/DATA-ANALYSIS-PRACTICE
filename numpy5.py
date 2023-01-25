#splitting the arrays 

import numpy as np 


#spliting is done by using the function array_split(array,splitvalue )


#array_split()  work when there are elements less than the requirement 

#splitting  can be done by the split() functions also 



a=np.array([23,45,56,54,34,56,4,5])
b=np.array_split(a,3)



print(b)

c=np.array_split(a,4)

print(c)


#splitting the arrays 

d=np.split(a,2)

print(d)


#display the subarrays 

print(d[1])
print(c[2])


#there is also a function of splitting called hsplit()   , 
#hsplit()  is a opposite function of the hstack()

e=np.hsplit(a,2)
print(e)


f=np.hstack((d,e))
print(f)




