#datatypes in the numpy 


# i =integer 
# u=unsigned integer 
# b=boolean 
# f=float 
# c=complex 
# S =string 
# U=unicode string 
#  O=object 
#  m=timedelta 
#  M=datetime 


import numpy as np
 
a=np.array([2.6,3,4,5.57896,6])

# finding the datatype of the array 

print(a.dtype)


#string array 

b=np.array(["h","45","sd"])

print(b)

print(b.dtype)


#creating array with the defined datatype 

c=np.array([23,45,67,78,2], dtype='f')

print(c.dtype)

#converting the datatype of the existing array 

a1=a.astype('i')

# here , i have coverte d the float vak=lues in the array to the integer values 

print(a1)

print(a.dtype)

####  copying the array 

a3=a.copy()

print(a3)

a3[3]=56

print(a3)

print(a)



#view of the array 

a4=a.view()

print(a4)

a4[2]=00

print(a4)
print(a)



# shaping the array 


#to know thw shape of the array 

print(a.shape)




#to change the shape of the array 

a.reshape(5)

print(a)


# to  to convert the 2 d array into the 1d array 

a.flatten()

print(a)






