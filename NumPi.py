import numpy as np

a = [1,2,3,4,5]

b = np.array(a)
#print(str(a)+ " "+ str(b))

#print(a*6)
#print(b*6)

ar = np.arange(10,101,2)
#print(ar.reshape((23,2)))

zeros = np.zeros((50, 10))
#print(zeros)

ones = np.ones((50,10))
#print(ones)

c = np.arange(1, 501, 8)
print(c.reshape((9,7)))