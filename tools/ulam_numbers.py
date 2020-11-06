def ulam_numbers(n: int) -> list:
    """
    Function returns the list of Ulam numbers of the given range.
    If parameter n is not an int function returns None.

    Ulam numbers sequence:
    1. Next Ulam number is bigger than the last one.
    2. Next Ulam is the sum of two previous Ulams.
    3. There's only one way to find the next Ulam.

    >>> ulam_numbers(10)
    [1, 2, 3, 4, 6, 8]
    >>> ulam_numbers(3)
    [1, 2]
    """

    # set basic ulam sequence
    ulam = [1, 2]
    next_ulam = 0

    # append next ulam to the list while ulam is less than n
    while next_ulam < n:
        all_sums = []

        # check every possible sum
        for pos in range(len(ulam) - 1):
            for p in range(pos + 1, len(ulam)):
                all_sums.append(ulam[pos] + ulam[p])
        
        all_sums.sort()

        # check if the sum is unique and greater than the last ulam
        for elem in all_sums:
            if elem > ulam[-1] and all_sums.count(elem) == 1:
                next_ulam = elem
                break

        ulam.append(next_ulam)

    return ulam[:-1]
