def qsort(array):
    greater=[]
    equal=[]
    smaller=[]
    
    if len(array)<= 1:
        return array
    
    p = array[0]
    
    for index in range(len(array)):
        if p<array[index]:
            greater.append(array[index])
        elif p>array[index]:
            smaller.append(array[index])
        else:
            equal.append(array[index])
            
    return qsort(smaller)+equal+qsort(greater)
