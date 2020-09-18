def create_array(size = 10, max =100):
    from random import randint
    return [randint(0,max) for _ in range(size)]

#Return the index of required element
def linear_search(sequence,start,num):
    if start >= len(sequence):
        return "Can't Find"
    elif (sequence[start] == num):
        return start + 1 #Return the index of element which is started from 1 (not 0)
    else:
        return linear_search(sequence,start+1,num)

a = create_array()
print (linear_search(a,0,7))
