import random
a=int(input("Enter no. of letters in password:"))
b=int(input("Enter no. of symbols in password:"))
c=int(input("Enter no. of digits in password:"))
Lsym=['*','/','+','-','_','^','&','<','>','~','|','?','!','@','#','$','%']
def letter(n):
    L=[]
    for i in range(n):
        x=random.randint(97,122)
        y=random.randint(1,2)
        if y==1:
            L.append(chr(x).upper())
        elif y==2:
            L.append(chr(x))
    return L
def symbol(n,ln):
    L=[]
    for i in range(n):
        x=random.randint(0,ln)
        L.append(Lsym[x])
    return L
def digit(n):
    L=[]
    for i in range(n):
        x=random.randint(0,9)
        L.append(str(x))
    return L
L1=letter(a)
L2=symbol(b,len(Lsym)-1)
L3=digit(c)
L1.extend(L2)
L1.extend(L3)
random.shuffle(L1)
Gen=''.join(L1)
print(Gen)
