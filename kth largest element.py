def largest_element(arr):
    arr.sort(reverse=True)
    return arr[k-1]

arr = [12, 3, 5, 7, 19]
k = 3
print(largest_element(arr))