#Binary search with no recursion

def binary_search(arr, val):
    left, right = 0, len(arr) - 1
    mid = left + (right - left)//2
    while left <= right:
        if val > arr[mid]:
            left = mid + 1
        elif val < arr[mid]:
            right = mid - 1
        else:
            return mid
        mid = left + (right - left) // 2
    return None
    






    

