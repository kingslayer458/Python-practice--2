def magical_tree(n):
    if n==1:
        return 1
    elif n==2:
        return 1+ 2
    
    branches = [1,2]

    for i in range(3,n+1):
        next_stage= 2* (branches[-1] * branches[-2])
        branches.append(next_stage)
    return sum(branches)

n = int(input("enter the number of stages: "))

print(magical_tree(n))