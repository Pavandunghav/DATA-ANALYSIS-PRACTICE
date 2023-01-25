
import numpy as np

a=np.array([23,45,67,78])

print(a)

b=np.array([24,65,45,78])

print(b)

print(a+b)


print(np.__version__)


#0d array (has only a single elements )






c=np.array(50)

print(c)


#1d array (has one dimension means atleast one row or the one column)

d=np.array([23,45,67,89])



print(d)

#2d array( it has one major array and inside it there are 2 arrays )


e=np.array([[23,45,67],[12,34,5],[8,9,70]])
print(e)




# 3d arrays   (are the 2 2ds array)


f=np.array([[[2,4,6],[4,6,8]],[[23,45,67],[76,57,89]]])
print(f)


#presents the dimensions 
print(f.ndim)

#present the size 
print(f.size)

#present the size 

print(f.shape)


#creating the array with n dimension 

g=np.array([45,67,2,3,4,6],ndmin=5)

print(g.ndim)



#accesing the  elements of the array 

print(a[0:],a[:2])
print(a[2]+a[1])


print(f[1,1],f[0,1])



#slicing 

print(a[1:3:1])