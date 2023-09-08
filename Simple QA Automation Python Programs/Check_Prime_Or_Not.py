#Natural Numbers: 1 and which has only 2 factors 1 and itself

#eg: 19 => 1 and 19 "prime no"
#28 => 1,2,4,7,14,28 => Not a prime number

number=28
count=0

if number>1:
    for i in range(1,number+1):
        if number%i==0:
            count=count+1
    if count==2:
        print('prime no')
        
    else:
        print('Not a prime')
            
            

