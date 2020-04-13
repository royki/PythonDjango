def sum_items(list1, list2):
    '''(list,list) -> list
    '''
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    return sum_list        
    


def count_matches(s1, s2):
    '''(str, str) -> int
    '''
    num_matches = 0
    for i in range(len(s1)):
        if(s1[i] == s2[i]):
            num_matches += 1
    return num_matches
