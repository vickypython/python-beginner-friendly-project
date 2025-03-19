def binary_search(list,target):
    first=0
    last=len(list)-1
    while first<=last:
        #look for the midpoint
        midpoint=(first+last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first=midpoint + 1
        else:
            last=midpoint -1
    return None
def verify(index):
    if index is not None:
        print('Target found:',index)
    else:
        print("Target not found")
numbers=[1,2,3,4,5,6,7,8,9]
results=binary_search(numbers,5)
verify(results)
numbers=[1,2,3,4,5,6,7,8,9]
results=binary_search(numbers,12)
verify(results)