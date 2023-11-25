from copy import copy


arr = [1,2,3,4]

def up(arr, index):
    if index-1>=0:
        elem = copy(arr[index])
        del arr[index]
        arr.insert(index-1, elem)
    
def down(arr, index):
    try:
        elem = copy(arr[index])
        del arr[index]
        arr.insert(index+1, elem)
    except:
        ...
    
    
up(arr,0)
print(arr)
