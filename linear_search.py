def linear_search(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Target found:',index)
    else:
        print("Target not found")
numbers=[1,2,3,4,5,6,7,8,9]
resuts=linear_search(numbers,5)
verify(resuts)
numbers=[1,2,3,4,5,6,7,8,9]
resuts=linear_search(numbers,12)
verify(resuts)
