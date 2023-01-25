#numpy 3  [iteration is arrays ]




# iterating in arrays

import numpy as np 

a=np.array([1,2,3,4,5,6,7])

for i in a:
    print(i,end=" ")
    
    
#iterating in 2D arrays 

b=np.array([[2,3,4,5,5],[34,56,345,88,112]])

for i in b:
    for j in i:
        print(j)
        
      
#here we used 2 for loops to display all the elements of the array 

#iterating in 3D array 

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])  

for i in c:
    for j in i:
        for k in j:
            print(k,end=" ")
            
            

#np.nditer using 

for i in np.nditer(c):
    print(i) 
    
    
#np.nditer is use to display all the elemnts in the array of any dimension 
#it reduces the time complexity 

for i in np.nditer(c):
    print(i)
    


#iterating with the steps :

for i in np.nditer(c[::2]):
    print(i)

        

    
#iterating with the index also 

for id, i in np.ndenumerate(c):
    print(id,i)
    

    
    
    
    

