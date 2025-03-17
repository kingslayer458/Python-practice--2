def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def sum_of_prime(N,M):
    total = 0
    for i in range(N,M+1):
        if is_prime(i):
            total += i
    return total

N=int(input())
M=int(input())
print(sum_of_prime(N,M))    

    