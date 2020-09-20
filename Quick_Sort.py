def create_array(size=10, max=100):
    from random import randint
    return [randint(0,max) for _ in range (size)]

def quick_sort(sequence):
    length = len(sequence)
    if (length <=1):
        return sequence
    else:
        pivot = sequence.pop()
    
    item_lower =[]
    item_greater = []
    for item in sequence:
        if (item <= pivot):
            item_lower.append(item)
        else: 
            item_greater.append(item)
    """
    This is descending order. For ascending order:
    Swapping the position into: quick_sort(item_greater) + ... + quick_sort(item_lower)
    """
    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)
sequence = create_array()
print(sequence)
print (quick_sort(sequence))