def merge_sort(x):
    """
    sorting an array with the recursive calls in the middle
    resulting array will be the ordered version of input.
    """
    # if the array only has 1 element:
    if len(x) <= 1:
        return x

    n = len(x)
    left_arr = merge_sort(x[:n//2])
    right_arr = merge_sort(x[n//2:])

    ordered = []
    lindex = 0
    rindex = 0

    # while the index is in range of left and right arrays
    while lindex < len(left_arr) and rindex < len(right_arr):
        # if the element on left array is smaller
        if left_arr[lindex]<right_arr[rindex]:
            ordered.append(left_arr[lindex])
            lindex += 1
        else:
            ordered.append(right_arr[rindex])
            rindex += 1

    # append any items left
    ordered.extend(left_arr[lindex:])
    ordered.extend(right_arr[rindex:])

    return ordered
