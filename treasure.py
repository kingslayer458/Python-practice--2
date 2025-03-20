n= int(input("enter the no of the element: "))

treasure_val= list(map(int,input("enter the treasure separated by spaces: ").split()))

max_value=max(treasure_val)
min_value=min(treasure_val)

diff=max_value-min_value

print("true value",diff)
