def get_answer(prompt):
    ''' (str) -> str
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer


def up_to_vowel(s):
    '''(str) -> str
    >>> up_to_vowel('hello')
    h
    >>> up_to_vowel('there')
    th
    '''
    # before_vowel contains all the characters found in s[0:i]
    before_vowel = ''
    i = 0

    # Accumulate the non-vowels at the beginning of the String.
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel

def last_vowel(s):
    ''' (str) -> str
    '''
    i = len(s) - 1
    while i >= 0:
        if s[i] in 'aeiouAEIOU':
            return s[i]
        i -= 1
    return None
