def count_inversion(array):
    """
    Aim: count all the inversions to create an ordered array
    Input: unordered array
    Output: ordered array
    """
    if len(array) <= 1:
        return array, 0

    # divide the array into 2:
    n = len(array)
    a, a_cnt = count_inversion(array[:n//2])
    b, b_cnt = count_inversion(array[n//2:])

    # total count:
    total_cnt = a_cnt + b_cnt

    # merging sorted arrays:
    lindex = 0
    rindex = 0
    ordered = []

    while lindex < len(a) and rindex < len(b):
        if a[lindex] <= b[rindex]:
            ordered.append(a[lindex])
            lindex += 1
        else:
            ordered.append(b[rindex])
            rindex += 1
            total_cnt += len(a) - lindex

    # add the remaning elements, if any left:

    ordered += a[lindex:]
    ordered += b[rindex:]

    return ordered, total_cnt
