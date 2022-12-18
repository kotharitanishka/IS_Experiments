pt = input("enter plain text : ").upper()
key = input("enter the key : ").upper()
print("entered values of plain text and key are  : " + str(pt) + " \n " + str(key))

k = 0
keystream = ""
for j in range(len(key)):
        ct = "".join(key[j])
        keystream += ct
        
for n in range(len(key), len(pt)):
        st = "".join(key[k])
        keystream += st
        k += 1
        if(k > 2):
            k = 0
        
print(keystream + " " + str(len(keystream)) + " " + str(len(pt)) + " " + str(len(key)))

def encryption(pt, keystream):
  encrypt_text = []
  for i in range(len(pt)):
    x = (ord(pt[i]) +ord(keystream[i])) % 26
    x += ord('A')
    encrypt_text.append(chr(x))
  return("" . join(encrypt_text))

def decryption(ct, keystream):
    orig_text = []
    for i in range(len(ct)):
        x = (ord(ct[i]) -
             ord(keystream[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

#keyStream = generateKey(pt , key)
ct = encryption(pt , keystream)
print("the encrypted cipher text is : "+ct)

ft = decryption(ct , keystream)
print("the decrypted plain text is : "+ ft)
