# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    ## repeat (numOfElements - 1) times
    #   set the first unsorted element as the minimum
    #   for each of the unsorted elements
    #     if element < currentMinimum
    #       set element as new minimum
    #   swap minimum with first unsorted position

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        ## loop thru the next element for comparison
        for j in range(i+1, len(arr)-2):
        ## compare two elements
            if arr[j] < arr[smallest_index]:
        ## rename the smallest element as smallest_index
                smallest_index = j
        # TO-DO: swap
        # Your code here
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    
    return arr


# TO-DO:  implement the Bubble Sort function below O(n^2)
def bubble_sort(arr):
    # Your code here
    ## Keep track of swaps, if no swaps end program
    ## compare the first and second elements
    ## if first is bigger, swap
    for i in range(len(arr) - 1):

        for j in (0, len(arr) - i - 1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
