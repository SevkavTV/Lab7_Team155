def happy_number_bool(n: int):
    '''
    Tells if number is happy
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    '''
    figures = list(str(n))
    while len(figures) != 1:
        result = 0
        for figure in figures:
            figure = int(figure)
            result += figure ** 2
        figures = list(str(result))
    if int(figures[0]) == 1:
        return True
    return False



def happy_numbers(n):
    '''
    Generates happy numbers in given 
    '''
    return [i for i in range(n) if happy_number_bool(i)]

