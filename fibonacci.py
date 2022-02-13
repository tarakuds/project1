import math

n = int(input("Please enter the integer value to check Fibonacci number: "))




def check_perfect_square(m):

    n = int(math.sqrt(m))

    return n*n == m

   

def check_fibo(m):

    return check_perfect_square(5*m*m + 4) or check_perfect_square(5*m*m - 4)

if(check_fibo(n) == True):

    print( n," is Fibonacci number")

else:

    print( n," is not a Fibnacci number")