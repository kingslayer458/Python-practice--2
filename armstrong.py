import math

def is_armstrong(n):
    num_digits=len(str(n))
    sum=0

    for digit in str(n):
        sum += math.pow(int(digit),num_digits)

    return sum == n
num =int(input("enter  a num"))

if is_armstrong(num):
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")
    



