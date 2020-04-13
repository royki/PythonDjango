'''
s = 'abccdeffggh'
for i in range(len(s) - 1):
    print(i)
'''

'''
def coutn_adjacent_repeats(s):
    repeats = 0
    for i in range(1, len(s)):
        if(s[i] == s[i-1]):
            repeats += 1
    return repeats
'''
def count_adjacent_repeats(s):
    ''' (str) -> int
    '''
    repeats = 0
    for i in range(len(s) - 1):
        if(s[i] == s[i+1]):
            repeats += 1
    return repeats

def count_adjacent_repeats1(s):
    ''' (str) -> int
    '''
    repeats = 0
    for i in range(1, len(s)):
        if(s[i] == s[i-1]):
            repeats += 1
    return repeats


def shift_left(lst):
    '''(list) -> NoneType
    '''
    first_item = lst[0]
    for i in range(1, len(lst)):
        lst[i-1] = lst[i]
    lst[-1] = first_item
    return lst
    

