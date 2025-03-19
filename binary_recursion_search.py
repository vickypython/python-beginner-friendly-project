def binary_recursion_search(list,target):
    #look if the list contain element or its null
    if len(list )==0:
        return False
    else:
        #list has element look for the midpoint
        midpoint=(len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                #do a recursive operation
                return binary_recursion_search(list[midpoint +1:],target)
            else:
                return binary_recursion_search(list[:midpoint],target)
def verify(index):
    if index is not None:
        print("Target found:",index)
    else:
        print("Target not found")
numbers=[1,2,3,4,5,6,7,8,9]
result=binary_recursion_search(numbers,5)
verify(result)
numbers=[1,2,3,4,5,6,7,8,9]
result=binary_recursion_search(numbers,12)
verify(result)