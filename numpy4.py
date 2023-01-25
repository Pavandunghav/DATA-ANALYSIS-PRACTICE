#numpy 4   [joining the arrays ]

import numpy as np

a=np.array([1,2,3,4,5,6],dtype='i')

b=np.array([2,3,4,5,6,7],dtype='i')


#to join the the two arrays we use the concatenate()  function 

c=np.concatenate((a,b))

print(c)
for i in np.nditer(c):
    print(i)


'''
#joining the 2D arrays

d=np.array([[2,3,4,5],[4,45,67,65,76]],dtype='i')
e=np.array([[34,56677,454,56],[2,1,1,1,11]],dtype='i')

f=np.concatenate((d,e))

for i in np.nditer(f):
    print(i)
    
    
    '''
    
#joining the arrays using the stack function 

g=np.stack((a,b))
print(g)

print(c)



#stacking along the horizontal is done by the hstack()

h=np.hstack((a,b))


#stcking in the vertical is done by the function vstack()
i=np.vstack((a,b))


#stacking in the height is done by the dstack()

j=np.dstack((a,b))



print(h)
print(i)
print(j)

