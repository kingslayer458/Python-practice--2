# Initialize an empty list
arr = []

# Take a list input (space-separated numbers)
name = input("Enter numbers: ").split()

# Convert the input strings to integers and store them in arr
arr = list(map(int, name))

# Reverse the list
arr.reverse()

# Print the reversed list
print(arr)
