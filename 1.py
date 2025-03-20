def sumofint(N,M):
    total= 0
    for i in range(N,M+1):
        total += i**3
        return total
N=int(input())
M=int(input())
print(sumofint(N,M))    