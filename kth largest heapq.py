import heapq

def heaplargest(arr,k):
    return heapq.nlargest(k,arr)[-1] 
    #return heapq.nsmallest(k,arr)[-1]

arr = [12, 3, 5, 7, 19]
k = 3
print(heaplargest(arr,k))  # Output: 19