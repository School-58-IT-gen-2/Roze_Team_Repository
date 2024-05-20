
p=0
while True:
    a=int(input())
    if a%3==0 and a%10==9:
        p+=a
    if a==0:
        break
print(p)
