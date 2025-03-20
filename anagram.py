def anagram(str1,str2):

    return sorted(str1) == sorted(str)

s1 = input("Enter first string: ").lower()  # Convert to lowercase for case insensitivity
s2 = input("Enter second string: ").lower()

# Checking and printing result
print("Anagrams" if anagram(s1, s2) else "Not Anagrams")