# Quick Sort
### Quicksort is a popular sorting algorithm that is often faster in practice compared to other sorting algorithms. It utilizes a divide-and-conquer strategy to quickly sort data items by dividing a large array into two smaller arrays. It was developed by Charles Antony Richard Hoare (commonly known as C.A.R.


### Pseudocode
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```



# Trace
### Sample Array: [8,2,7,3]

### passe1 : povid = 3 , left = [2], right =[8,7]
### take the right and comparted it with the hole array star from the left
### depending on the right it will divide the  array in to three parts( in the left we will put the values less than the right , in the right we will put the value that bigger than the right , the right it self )
### passe2 : povid = 2
### reapet the same procces for the left side
### passe3 :  povid = 7 , right = 8
### reapet the same procces for the left side
### passe 4 : arr = [2,3,7,8]
### merge the sorted left with the povid and the right side and put them in one array

# Efficency
- Time: O(nlog n)
- Space: O(1)
