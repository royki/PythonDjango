def get_answer(prompt):
    ''' (str) -> str
    '''
    answer = input(prompt)
    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)
    return answer

def up_to_vowels(s):
    ''' (str) -> str

    Return a substring of s from index 0 upto but not including the first vowel in s.

    >>> up_to_vowels("hello")
    'h'
    >>> up_to_vowels("there")
    'th'
    >>> up_to_vowels("cs")
    'cs'
    '''
    # before_vowels contains all the characters found in s[0:1]    
    before_vowel = ''
    i = 0

    # Accumulate the non-vowels at the beginning of the string
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1
    return before_vowel
