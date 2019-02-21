def max_number(i: float, j: float, k: float)->int:
    '''
    This method returns the largest of three numbers.
    '''
    if(i > j):
        if(i > k):
            return i
        else:
            return k
    else:
        if(j > k):
            return j
        else:
            return k
