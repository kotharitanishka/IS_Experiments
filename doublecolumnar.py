import numpy as np

pt = input("enter plain text : ").replace(" " , "").upper()
key = input("enter key : ").replace(" " , "").upper()

def encrypt(pt, key):

    lpt = len(pt)
    lkey = len(key)
    col = lkey

    l1 = list(pt)
    l2 = list(key)

    if(lpt % lkey == 0):
        rows = int(lpt/lkey)
    else:
        rows = int(lpt/lkey) + 1

    extra = lpt%lkey

    for i in range(extra):
        l1.append('X')

    arr_1d = np.array(l1)
    arr_2d = np.reshape(arr_1d, (rows,col))

    x = sorted(l2)

    order = []
    for i in range(len(l2)):
        order.append(l2.index(x[i]))

    ct = []

    for i in range(col):
        col_index = order[i]
        for j in range(rows):
            ct.append(arr_2d[j][col_index])
            
    ciphert = ''.join(ct)
    return(ciphert)

ct = encrypt(pt , key)
print("the encrypted cipher text is : " + ct)



def decry(ct,key):
      
    lpt = len(ct)
    lkey = len(key)
    col = lkey

    l1 = list(ct)
    l2 = list(key)

    if(lpt % lkey == 0):
        rows = int(lpt/lkey)
    else:
        rows = int(lpt/lkey) + 1

    x = sorted(l2)
      
    od = []
    for i in range(len(l2)):
        od.append(x.index(l2[i]))

    d_arr_1d = np.array(l1)
    d_arr_2d = np.reshape(d_arr_1d, (col,rows))
    de_arr2d = d_arr_2d.transpose()
    finalllyyyy = de_arr2d[:, od]
    
    dt = []
    for i in range(rows):
        for j in range(col):
            dt.append(finalllyyyy[i][j])
    
    dt = dt[: len(ct)]
    dplain = ''.join(dt)
    return(dplain)


key2 = input("enter key : ").replace(" " , "").upper()

ct2 = encrypt(ct , key2)
print("the double encrypted cipher text is : " + ct2)

ft = decry(ct2 , key2)
print("the first decrypted plain text is : " + ft)

ftt = decry(ft , key)[:len(pt)]
print("the double decrypted plain text is : " + ftt)