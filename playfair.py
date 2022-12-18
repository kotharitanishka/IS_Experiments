import numpy as np

pt = input("enter pt : ").replace(" ", "").upper()
key = input("enter key : ").replace(" ", "").upper()

l1 = list(key)
lkey = len(key)
lenpt = len(pt)
lpt = list(pt)

for i in range(lenpt):
    if(i < lenpt-1):
        if(lpt[i] == lpt[i+1]):
            lpt.insert(i+1, 'X')
            print(lpt)

if(lenpt % 2 != 0):
    lpt.append('X')
    print(lpt)

s = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
l2 = list(s)

a = set(l1)
b = set(l2)
c = set(l2) - set(l1)

l3 = list(c)

x = sorted(l1)
y = sorted(l3)

l4 = []
l4 = l1 + y

arr_1d = np.array(l4)
arr_2d = np.reshape(arr_1d, (5, 5))
print(arr_2d)

def indexOf(ele,arr_2d):
    result = np.where(arr_2d == ele)
    
    listOfCoordinates= list(zip(result[0], result[1]))
    return(listOfCoordinates[0])


def encryptDecrypt(pt,matrix , isDecrypt):
    inc=1
    if isDecrypt:
        inc=-1
    ct = ''
    for  (i,j) in zip(pt[0::2], pt[1::2]):
        r1,c1 = indexOf(i,matrix)
        r2,c2 = indexOf(j , matrix)

        if c1==c2:
            ct+= matrix[(r1+inc) % 5][c1] + matrix[(r2+inc)% 5][c2]
        elif r1==r2:
            ct+= matrix[r1][(c1+inc) % 5] + matrix[r2][(c2 + inc)  % 5]
        else:
            ct+= matrix[r1][c2] + matrix[r2][c1]
    return ct


ct = encryptDecrypt(lpt,arr_2d , isDecrypt=False)
print(ct)
pt = encryptDecrypt(ct , arr_2d , isDecrypt=True)
print(pt)


