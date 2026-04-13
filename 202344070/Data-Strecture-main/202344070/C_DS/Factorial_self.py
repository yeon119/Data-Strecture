def factorial(n): 
    if(n==1) :
        return 1
    
    else :
        return n*factorial(n-1)

n = 10
print('%d! =' %n,factorial(n))