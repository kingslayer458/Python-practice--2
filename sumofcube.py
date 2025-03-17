def cube_sum(N,M):
    total = 0
    for i in range(N,M+1):
          total += i**3  # Add the cube of each number
    return total
      

N=int(input())
M=int(input())
print(cube_sum(N,M))