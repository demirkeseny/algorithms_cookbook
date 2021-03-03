def finding_smallest(array):
    """
    Finds the smallest value in the array and returns its index
    """
    # if only 1 element, return its index
    if len(array) == 1:
        return 0

    # accept the first value as the smallest
    smallest = array[0]
    idx_smallest = 0

    for i in range(1,len(array)):
        if array[i]<smallest:
            smallest=array[i]
            idx_smallest=i
    return idx_smallest

def selection_sort(array):
    """
    Sorting the list in ascending order
    1. Create an empty list
    2. Iterate through the list to find the smallest
    3. Delete that element from the earlier list
    """

    new_lst=[]

    for i in range(0,len(array)):
        smallest=finding_smallest(array)
        new_lst.append(array.pop(smallest))
    return new_lst
