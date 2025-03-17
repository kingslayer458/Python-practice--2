def second_largest(arr):
    uniq  = list(set(arr))

    if len(uniq) < 2:
        return -1
    uniq.sort()

    return uniq[-2]

cy=list(map(int,input("enter: ").split()))
print(second_largest(cy))