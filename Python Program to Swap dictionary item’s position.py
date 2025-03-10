data = {'Gfg': 4, 'is': 1, 'best': 8, 'for': 10, 'geeks': 9}

print("initia Dictionary items:",data)

i,j = 1, 3

tups = list(data.items()) #for list use data.items()

tups[i], tups[j] = tups[j], tups[i]
 
# converting back
res = dict(tups) 
 
# printing result
print("The swapped dictionary : " + str(res))