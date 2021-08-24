number = int(input())
temp = number
reverse=0
while temp>0:
    
    remainder = temp%10
    reverse = (reverse*10) + remainder
    temp = temp//10
    
if number == reverse :
    print ("true")
else:
    print ("false")
