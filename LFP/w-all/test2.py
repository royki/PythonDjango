def double_even_indices(lst):
    '''(list of int) -> NoneType
    '''
    i = 0
    while i < len(lst):
        lst[i] = lst[i]*2
        i = i + 2


def double_first_element(lst):
    if len(lst) > 0:
        lst[0] = lst[0] * 2


s = 'computer science'
'''
len(s)
for i in range(len(s)):
    print(i)

print("---------")    

for i in range(1, len(s)):
    print (i)

print("---------")    

for i in range(2, len(s), 2):
    print(i)
    

print("---------")     
'''


def print_every_third_char(s):
    for i in range(0, len(s), 3):
        #print(s[i])
        print(s[i:i+1])
