# Creating an array randomly
def create_array(size = 10, max =100):
    from random import randint
    return [randint(0,max) for _ in range(size)]

# Sorting the array (quick sort)
def sorting (sequence):
    length = len(sequence)
    if (length <= 1):
        return sequence
    else:
        pivot = sequence.pop()
    item_lower = []
    item_greater = []
    for item in sequence:
        if (item <= pivot):
            item_lower.append(item)
        else:
            item_greater.append(item)
    return sorting(item_lower) + [pivot] + sorting(item_greater)

# Returning the index of required element after the array was sorted
def binary_search(sequence,lower,greater,key):
    
    if (lower > greater):
        return "Can't find"
    else:
        mid = (lower + greater) //2
    if (key == sequence[mid]):
        return mid+1
    elif (key > sequence[mid]):
        return binary_search(sequence,lower+1,greater,key)
    else:
        return binary_search(sequence,lower,greater-1,key)
a = create_array()
print (a)
a = sorting(a)
print (a)
print (binary_search(a,0,len(a)-1,11))