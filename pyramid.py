def pyramid(n):
    for i in range(1,n+1):
        spaces=' ' *(n-i)
        stars ='*' *(2*i-1)
        print(spaces+stars)
n=int(input("enter"))
print(pyramid(n))
