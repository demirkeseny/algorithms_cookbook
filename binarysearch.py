def binary_search(array, item):
    """
    Input: sorted array and integer
    Output: the position, which is assigned by item, from the the ordered array
    """
    low = 0
    high = len(array)-1

    while low <= high: # the array shouldn't consist of 1 element
        mid = (low + high)//2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid-1
        else:
            low=mid+1
    return None
    
