n=int(input())
d=2
i = 0

while n>d :
    if n%d==0 :
        i+=1
        print ("divisible by",d, "and count",i)
    else:
        print ("not divisible by this number",d)

     

    d+=1

    
