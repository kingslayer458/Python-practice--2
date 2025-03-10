def number_pyramid(n):
    for row in range(1,n+1):
      for i in range(row):
         print(row,end=" ")
      print()

# Taking input
n = int(input("Enter N: ").strip())

# Calling function
number_pyramid(n)