n=int(input())

k=2

while n>=k :
    d=2
    flag = False
    while k>d :
        if k%d==0 :
            flag = True
        d+=1
    
    if not(flag):
        print (k)
    k= k+1
    





