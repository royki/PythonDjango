def is_palindrom_v1(s):
    '''(str) -> bool

    Return true iff s is a palindrom
    
    >>> is_palindrom_v1('noon')
    True
    >>> is_palindrom_v1('racecar')
    True
    >>> is_palindrom_v1('dented')
    False
    '''

    return reverse(s) == s


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

if __name__ == '__main__':
    print('Version 1', __name__)

    word = input('Enter a word: ')
    if is_palindrom_v1(word):
        print(word, ' is a palindrom')
    else:
        print(word, ' is not a palindrom')