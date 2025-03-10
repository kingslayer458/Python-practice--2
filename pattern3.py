def forest(n):
    for row in range(1,n+1):
        for num in range(1,row+1):
            print(num,end=" ")
        print()
      
            
n=int(input("enter: ").strip())        
forest(n)
