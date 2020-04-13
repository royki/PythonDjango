def countStringInList(string_list, n):
    """(list, int) -> list
    find n number of strings from the list of string
    using dictionary from getElementsDictionary function

    >>> string_list = ['red', 'red', 'blue', 'yellow', 'blue']
    >>> countStringInList(string_list, 2)
    ['red','blue']
    >>> countStringInList(string_list, 1)
    ['yellow']
    >>> countStringInList(string_list, 3)
    []
    """    
    dic = getElementsDictionary(string_list)
    key for key, value in dic.items():
        if value == n:
            return key
    keys = [key for key, value in dic.items() if value == n]
    print(keys)
    # for key, value in dict.items():
    #     if value == n:            
    #         return (key)
    key for key, value in dic.items():
        if value == n:
            return key
    
    
def getElementsDictionary(string_list):
    """(list) -> dictionary
    count the number of elements from the list and return in dictionary
    >>> string_list = ['red', 'red', 'blue', 'yellow', 'blue']
    >>> getElementsDictionary(string_list)
    {'red': 2, 'blue': 2, 'yellow': 1}
    >>> string_list = ['red', 'blue', 'yellow']
    {'red': 1, 'blue': 1, 'yellow': 1}
    """
    elements = {}
    for elem in string_list:
        if elem in elements.keys():
            elements[elem] += 1
        else:
            elements[elem] = 1
    return elements
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
import unittest
import countStringInList

class testCountStringInList(unittest.TestCase):
    string_list = ['red', 'red', 'blue', 'yellow', 'blue']
    def testCountStringInList_1(self):
        actual = countStringInList(string_list,2)
        expected = ['red', 'blue']
        self.assertEqual(actual, expected)
        
    def testCountStringInList_2(self):
        actual = countStringInList(string_list,1)
        expected = ['yellow']
        self.assertEqual(actual, expected)
        
    def testCountStringInList_1(self):
        actual = countStringInList(string_list,3)
        expected = []
        self.assertEqual(actual, expected)

    def testCountStringInList_1(self):
        actual = countStringInList(string_list,0)
        expected = []
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)


def is_balanced(paren):
    """
    list(str) -> str
    Return a boolean value true if parenthesis are balanced; otherwise false.
    is balanced indicates true value and is NOT balanced indicates false.
    >>> is_balanced("()()()()")
    is balanced
    >>> is_balanced(")()()()(")
    is NOT balanced
    >>> is_balanced("((())())")
    is balanced
    >>> is_balanced("(((((())")
    is NOT balanced
    """
    stack = []
    parenthesis = list(paren)
    dic = {'(':')'}
    # dic = {'(':')', '{':'}', '[':']'} # considering all kind of parenthesis
    
    for p in parenthesis:
        if p in dic.keys():
            stack.append(p)
        elif p in dic.values() and len(stack) > 0:
            c = stack.pop()
            if dic.get(c) != p:
                return "is Not Balanced"
        else:
            return " is Not Balanced"
            
    if len(stack) == 0:
        return "is Balanced"
    else: 
        return "is Not Balanced"

if __name__ == '__main__':
    import doctest
    doctest.testmod()


import unittest
import is_balanced
class testIsBalancedTest(unittest.TestCase):
    
    def testIsBalancedTest_1(self):
        actual = is_balanced("()")
        expected = "is balanced"
        self.asert(actual, expected)
        
    
    def testIsBalancedTest_2(self):
        actual = is_balanced("{}")
        expected = "is balanced"
        self.asert(actual, expected)
    
    def testIsBalancedTest_3(self):
        actual = is_balanced("[]")
        expected = "is balanced"
        self.asert(actual, expected)
        
    def testIsBalancedTest_4(self):
        actual = is_balanced("[{()}]")
        expected = "is balanced"
        self.asert(actual, expected)
    
    def testIsBalancedTest_4(self):
        actual = is_balanced("([{]")
        expected = "is NOT balanced"
        self.asert(actual, expected)
    
    def testIsBalancedTest_5(self):
        actual = is_balanced("([](){}")
        expected = "is NOT balanced"
        self.asert(actual, expected)
        
    def testIsBalancedTest_6(self):
        actual = is_balanced(")()()()(")
        expected = "is NOT balanced"
        self.asert(actual, expected)
        
    def testIsBalancedTest_7(self):
        actual = is_balanced("()()()()")
        expected = "is balanced"
        self.asert(actual, expected)
            
    def testIsBalancedTest_8(self):
        actual = is_balanced("((())())")
        expected = "is balanced"
        self.asert(actual, expected)
        
    def testIsBalancedTest_9(self):
        actual = is_balanced("(((((())")
        expected = "is NOT balanced"
        self.asert(actual, expected)
        
    
    def testIsBalancedTest_(self):
        actual = is_balanced("([(90)]")
        expected = "is NOT balanced"
        self.asert(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
        

https://www.interviewzen.com/interview/4gZxp6R