# Selection sort is stupidly easy. In selection sort all you have to do is
# Select the smallest value in the subarray to the right and fit it in the subarray in the
# left. 
def selection_sort(arr):
    for i in range(len(arr)):
        #find the smallest in the subarray to the right
        j = i
        min_index = i
        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

                
     
            


