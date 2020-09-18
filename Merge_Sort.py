#Creating a array randomly
def create_array(size = 10, max = 100):
    from random import randint
    return [randint(0,max) for _ in range (size)]

# Merge each list sequence 1 and sequence 2 
def merge(seq1, seq2):
    result = []
    seq1_index, seq2_index = 0,0
    while (seq1_index < len(seq1) and seq2_index < len(seq2)):
        if (seq1[seq1_index] < seq2[seq2_index]):
            result.append(seq1[seq1_index])
            seq1_index += 1 
        else:
            result.append(seq2[seq2_index])
            seq2_index += 1 
    if seq1_index == len(seq1): 
        result.extend(seq2[seq2_index:])
    elif (seq2_index ==len(seq2)):
        result.extend(seq1[seq1_index:])
    return result

#Sorting
def merge_sort(sequence):
    if (len(sequence)<=1 ):
        return sequence
    a = len(sequence)//2
    left = merge_sort(sequence[:a])
    right = merge_sort(sequence[a:])
    return merge(left, right)
#Main
array = create_array()
print (array)
print (merge_sort(array))
