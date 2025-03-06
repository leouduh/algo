# This is one is not memory efficient you are basically using copies
def quick_sort_bad(arr):
    if len(arr) < 2:
        return arr
    i, j = -1, 0
    pivot = arr[len(arr)-1]
    #position the pivot where it belongs using the algorithm below
    while(j < len(arr) - 1):
        if arr[j] < pivot:
            #increment
            i += 1
            #swap
            arr[j], arr[i] = arr[i], arr[j]
        j += 1
    #swap and increment when you get to the end
    i += 1
    arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]

    #pivot index in now i
    #now that you have placed the pivot wher it belongs do this recursively
    return quick_sort_bad(arr[0:i]) + arr[i:i+1] + quick_sort_bad(arr[i+1:])



def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i, j = low - 1, low
        while(j < high):
            if arr[j] < pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
        arr[i], arr[high] = arr[high], arr[i]

        #recursively call quicksort
        quick_sort(arr, low, i-1)
        quick_sort(arr, i+1, high)
        return arr

        


l = [10, 0, 2, 5, 3 ,7, 8, 1]
print(quick_sort(l, 0, len(l)-1))

