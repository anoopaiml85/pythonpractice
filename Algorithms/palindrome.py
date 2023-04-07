s = 'malayalam'

def is_palindrome(s):
    return s == s[::-1]


#print('The sring is palindrome' f{is_palindrome(s),s[0:-1]})
print(f'The sring is palindrome. {is_palindrome(s)}{s[::-1]}')