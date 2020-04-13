def count_vowels(s):
    ''' (str) -> int
    Return the number of vowels in s. Don't treat the letter y as a vowel
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''    
    num_vowels = 0
    for c in s:
        if c in 'aeiouAEIOU':
            num_vowels = num_vowels + 1            
    return num_vowels


def has_vowel(s):
    """(str) -> bool
    Return True if and only if s has at least one vowel, not including y.
    >>> has_vowel("Anniversary")
    True
    >>> has_vowel("xyz")
    False
    """
    vowel_found = False
    for char in s:
        if char in 'aeiouAEIOU':  
           return True
    return vowel_found
