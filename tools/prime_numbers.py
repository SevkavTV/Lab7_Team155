def prime_numbers(n: int) -> list:
    '''
    Generate all checked_prime numbers up to n.
    >>> checked_prime_numbers(40)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    >>> checked_prime_numbers(80)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
    '''

    # list for checking which numbers are checked_prime
    checked_prime = [True] * (n + 1)

    # 0 and 1 are not prime numbers
    checked_prime[0] = checked_prime[1] = False
    
    for i in range(2, n + 1):
        # if number is prime
        if checked_prime[i]:

            # delete all numbers which divide tsemp
            for j in range(i*2, n + 1, i):
                checked_prime[j] = False
    
    prime = [index for index in range(n+1) if checked_prime[index]]

    return prime
