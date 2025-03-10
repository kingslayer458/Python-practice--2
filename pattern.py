def forest(n):
    for row in range(n):
        for col in range(n):
            print("* ",end=" ")
        print()    
            
n=int(input("enter: ").strip())        
forest(n)