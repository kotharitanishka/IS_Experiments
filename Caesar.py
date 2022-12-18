s = "abcdefghijklmnopqrstuvwxyz"

def encry(pt, key):
    op = ''
    for i in range(len(pt)):
        x = s.index(pt[i])
        x = (x + key) % 26
        ct = "".join(s[x])
        op += ct
    print("the encrypted cipher text is : " + op)
    return op

def decry(dt, key):
    opp = ''
    for i in range(len(dt)):
        y = s.index(dt[i])
        y = (y - key) % 26
        ptt = "".join(s[y])
        opp += ptt
    print("the decrypted text is : " + opp)

pt = input("enter plain text : ").lower()
key = int(input("enter the key : "))
print("the plain text is : " + pt + " and key is : " + str(key))
x = encry(pt, key)

# dt = input("enter text to decrpt : ").lower()
# key = int(input("enter the key : "))
# print("the plain text is : " + dt + " and key is : " + str(key))
# decry(dt, key)

print("the new plain text is : " + x + " and key is : " + str(key))
decry(x, key)