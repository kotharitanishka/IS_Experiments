
def to_binary(pt):
    ct = ''
    for char in list(pt):
        asc = ord(char)
        ct+=str(bin(asc)[2:])

    return ct

def make_blocks(ct, key):
    ct_list = []
    size = len(key)
    n = len(ct)//len(key)
    for i in range(n):
        ct_list.append(ct[i*size:(i+1)*size])
    return ct_list

def single_xor(block , key):
    result = []
    c = list(map(int, block))
    k = list(map(int, key))
    for i, j in zip(c, k):
        result += [str(i^j)]
    return ''.join(result)

def encrypt(blocks , key):
    res = []
    for block in blocks:
        res+= single_xor(block , key)
    res = ''.join(res)

pt = input("Enter PT : ") * (10 ** 2)
key = input("Enter key in binrary : ")
pt = to_binary(pt)
blocks = make_blocks(pt , key)
encrypt(blocks , key)