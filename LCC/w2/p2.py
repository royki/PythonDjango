import p1

def is_palindrom_v2(s):
    '''(str) -> bool

    Return true iff s is a palindrom
    
    >>> is_palindrom_v2('noon')
    True
    >>> is_palindrom_v2('racecar')
    True
    >>> is_palindrom_v2('dented')
    False
    '''
    # The number of chars in s.    
    n =len(s)
    # Compare the first half of s to the revers of the second half.
    # Omit the middle character of an odd-length string.
    return s[:n // 2] == reverse(s[n - n //2:])
    

def reverse(s):
    '''(str) -> str
    Return a reversed version of s.
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    '''

    rev = ''

    # For each character in s, add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev
    return rev

print('Version 2', __name__)
