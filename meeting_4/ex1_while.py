

x = int(input("x="))
l=[]

while x > 0:
    r = x % 2
    l.append(r)
    x //= 2


print(l[::-1])