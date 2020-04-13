def is_palindrom_v3(s):
    '''(str) -> bool

    Return true iff s is a palindrom
    
    >>> is_palindrom_v3('noon')
    True
    >>> is_palindrom_v3('racecar')
    True
    >>> is_palindrom_v3('dented')
    False
    '''

    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    return j <= i
    
        
