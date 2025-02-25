#Gist: Inserting the first element of an unsorted sub array into the sorted
#sub array


# The way insertion sort works is very trivial

# You have a sorted sub array to the left and an unsorted subarray to the right

# You pick the first element from the unsorted array (say 'b') 
# and place it where  It belongs in the sorted array.

# All you have to do is make sure the element 'b' is bigger than the last 
# element in the sorted array if that is true then b is now a part of the 
# sorted sub array and you move to the next index in the array

# exammple

# 1, 2, 5, 4, 3

# In this example 1, 2, 5 are the sorted subarray. 4 is what we need so sort
# csince 4 is < 5 we will swap them

# 1, 2, 4 ,5, 3
# Now we have this looking at this 4 is not < 2 so we cannot continue since
#everything to the left of 4 up to the pos of where 4 was is now sorted

# Lastly we need to insert the last element in the unsorted array 3 into the 
# sorted array. 

#We accomplish this by moving 3 left and swapping if what we are comparing is
#Greater

#1, 2, 4, 3, 5
#1, 2, 3, 4, 5


#Code:
def insertion_sort(arr):
    # iterate through the array
    for i in range(1, len(arr)):
        #first element of the unsorted list
        j = i
        # while the first element of the unsorted list is less than the 
        # elements to its left we keep searching till we insert it in its right
        # position
        while(j >= 0 and (arr[j] < arr[j-1])):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

#Test
print(insertion_sort([1, 2, 4, 5, 3]))

