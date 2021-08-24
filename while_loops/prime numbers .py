n=int(input())
d=2
flag = False

while n>d :
    if n%d==0 :
        flag = True

    d+=1

    
if flag:
    print ("not prime")

else:
    print ("prime")
    
