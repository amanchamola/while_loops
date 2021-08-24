number = int(input())
temp = number
sumodd=0
sumeven=0
reverse=0
while temp>0:
    
    remainder = temp%10
    if remainder%2==0:
        sumeven=sumeven+remainder

    else:
        sumodd=sumodd+remainder
     
    temp = temp//10

print (sumeven,sumodd)

    
