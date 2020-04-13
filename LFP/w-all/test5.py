def calculate_average(asn_grades):
    '''(list of [str, num]) -> float
    '''
    total = 0
    for item in asn_grades:
        total += item[1]
    return total / len(asn_grades)



'''
for metal in ['Li', 'Na']:
	for gas in ['F', 'Cl', 'Br']:
		print(metal + gas)
'''

def average(grades):
    '''
    (list of list of number) -> list of float
        Return a new list in which each item is the average of the grades in the inner list at
        the corresponding position of grades.
        >>> grades = [[70, 80, 75], [70, 80, 90, 100], [80, 100]]
    eng = grades[0]
    '''

    averages = []
    for grades_list in grades:
        # calculate the average of grades_list and append it to average
        total = 0
        for mark in grades_list:
            total += mark
        averages.append(total / len(grades_list))
    return averages        

def mystery(lst):
    for sublist in lst:
        total = 0
        for num in sublist:
            total += num
    return total
