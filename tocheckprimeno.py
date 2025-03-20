def is_prime(n):
    if n < 1:
        return False
    for i in range(2,int(0.5**2)+1):
        if n % i==0:
            return False
    return True

num= int(input("enter the prime number:"))

if is_prime(num):
    print(num)
else:
    print(f"its{num} not")    