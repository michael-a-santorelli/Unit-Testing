'''
This script runs test cases for the max_number method.
The tests run include black-box and white-box unit testing.
'''

# black-box unit tests
'''
Only 1 test is necessary for black-box testing.
The specification only states that the method returns the largest number.
'''
# example of black-box test case
result1 = max_number(1,2,3)
expected1 = 3

if(result1 == expected1):
    print("Black-Box Testing Result: Pass!")
else:
    print("Black-Box Testing Result: Fail!")

# white-box unit tests
'''
The white-box testing has 4 cases.
The 4 cases come from the 4 paths through the conditionals.
'''
# i > j and i > k
result2 = max_number(9, 2, 1)
expected2 = 9

# i > j but i < k
result3 = max_number(5, 1, 7)
expected3 = 7

# i < j and j > k
result4 = max_number(1, 3, 2)
expected4 = 3

# i < j but k > j
result5 = max_number(1, 2, 3)
expected5 = 3

if(result2 == expected2 and result3 == expected3 and result4 == expected4 and result5 == expected5):
    print("White-Box Testing Result: Pass!")
else:
    print("White-Box Testing Result: Fail!")
