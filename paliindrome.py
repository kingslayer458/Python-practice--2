def is_pallindrome(s):
    return s == s[::-1]

s= input("enter a string").lower()
print("pallindrome" if is_pallindrome(s) else "no")