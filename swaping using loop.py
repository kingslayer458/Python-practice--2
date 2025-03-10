



# Original dictionary
original_dict = {'Gfg': 4, 'is': 1, 'best': 8, 'for': 10, 'geeks': 9}
 
# Create an empty dictionary to store the swapped items
swapped_dict = {}
 
# Swap the positions of items using a loop
for key, value in original_dict.items():
    swapped_dict[value] = key
 
# Print the swapped dictionary
print("The swapped dictionary :", swapped_dict)