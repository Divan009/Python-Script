

from random import randint

def generate():
    return(randint(0,100))
    
def isPrime():
    num = generate()
    if num>1:
        #Iterate from 2 to n/2
        for i in range(2,num//2):
            #if num is divisible by any number between
            # 2 and n/2, not a prime num
            if (num % i) == 0:
                break
        else:
            print(num)
            
    else: 
        print("nah")


isPrime()
    
# Almost Same code in  line
# in love with Python


a = [x for x in range(0,100) if all(x % y != 0 for y in range(2,x))]
