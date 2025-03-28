def merge_sort(list):
    #divide:find the midpoint and divide into sublist
    #conquer:recusively sort the sublist created in previous step
    #combine:merge the sorted sublists created in previous step
    #base case or stopping condition
    if len(list)<=1:
        return list
    #divide
    left_half,right_half=split(list)
    #conquer
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    #combine the sorted sublists into one list
    return merge(left,right)
def split(list):
    """
    divide the unsorted list at midpoint into sublist
    return the sublists -left and right
    """
    midpoint=len(list)//2
    left=list[:midpoint]
    right=list[midpoint:]
    return left,right
def merge(left,right):
    """
    merges two lists ,sorting them in the process
    return a new merged list
    """
    l=[]
    #i for index in left
    i=0
    #j for the index in right
    j=0
    while i< len(left) and j<len(right):
        if left[i]< right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[i])
            j+=1
    while i < len(left):
        l.append(left[i])
        i+=1
    while j<len(right):
        l.append(right[i])
        j+=1