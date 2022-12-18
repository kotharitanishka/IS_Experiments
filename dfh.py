print("enter the value of modulus p , base g , secret key of alice , secret key of bob")
p, g, a, b = [int(x) for x in input("enter 4 numbers : ").split(",")]
print("entered values of p g a b are  : " + str(p) +  " " + str(g) +  " " + str(a)+  " " + str(b))

xa = pow(g,a,p)
xb = pow(g,b,p)
print("value of xa , xb is  : " + str(xa)  +  " " + str(xb))

ak = pow(xb, a, p)
print("the secret key of alice ak is  : " + str(ak))
bk = pow(xa, b, p)
print("the secret key of bob bk is  : " + str(bk))

if(ak == bk):
    print("good to go")
else:
    print("kuch toh gadbad hai")
