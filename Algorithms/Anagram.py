'''Write a function that takes two strings as input and returns True if they are anagrams
 (contain the same letters in a different order), and False otherwise.'''

str1='tell'
str2='let'
# print(sorted(str1))
# print(sorted(str2))
if (len(str1) == len(str2)):
    print("checking if the strings is anagrams.")    
    if (sorted(str1)==sorted(str2)):
        print('The two strings are Anagrams')
    else: 
        print('The two strings are not anagrams') 
else:
    print("Length of strings not equal.Not an anagram")           