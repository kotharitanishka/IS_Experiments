# Steps: 
# Take a string p. Calculate the Length of the string. Convert that length to the nearest prime number value. 
# Take another string q (Passphrase). Calculate its length. Convert the length to the nearest prime number value. 
# Make sure both p and q are different, If not change the value of q to the immediate next prime number 
# Calculate n=p*q 
# Calculate Totient Function(phi) =(p-1)(q-1) 
# Select e such that it is relatively prime to phi. 
# Calculate d using the formula : 
# (d*e)mod phi ≡ 1 
# Perform Encryption: CT = (PT)e mod n 
# Perform Decryption: PT =(CT)d mod n 

from math import gcd

p = input("enter string p : ")
q = input("enter string q : ")

print("entered strings are : \n" + p + "\n" + q)

lp = len(p)
lq = len(q)

def check_prime(n):
    flag = 1
    if(n>1):
        for i in range(2,n):
            if(n % i == 0):
                flag = 1
                break
            else:
                flag = 0
    # if(flag == 0):
    #     print(str(n) + " is prime")
    # elif(flag==1):
    #     print(str(n) + " is not prime")
    return flag

pp = check_prime(lp)
pq = check_prime(lq)

def smallest_prime(num):
    for i in range (num-1, 2, -1):
        y = check_prime(i)
        if(y == 0):
            return i
    
def next_prime(num):
    for j in range(num+1,99999):
        z = check_prime(j)
        if(z==0):
            return j
   
if(pp == 1):
    lp = smallest_prime(lp)
    # print(lp)

if(pq == 1):
    lq = smallest_prime(lq)
    # print(lq)
    
if(lp == lq):
    lq = next_prime(lq)
    
print("new value of p is : " + str(lp))
print("new value of q is : " + str(lq))

n = (lp * lq) # type: ignore
print("value of n is : " + str(n))

phi = (lp - 1)*(lq - 1) # type: ignore
print("value of phi is : " + str(phi))

e = 0
d = 0
for i in range (2 , phi):
    if( gcd(i,phi)==1 and i!=lp and i!=lq ):
        e = i
        break   
     
for i in range (2 , phi):
    if( (i*e)%phi==1 and i!=e ):
        d = i
        break
    
print("value of e is : " + str(e))
print("value of d is : " + str(d))
    
    
pt = int(input("enter the plain text : "))

if(pt > phi): 
    pt = pt%phi
    print("since pt > phi , taking mod")

print("new pt is : " + str(pt))

ct = pow(pt,e,n)
print("ct is : " + str(ct))

decry = pow(ct,d,n)
print("decry is : " + str(decry))