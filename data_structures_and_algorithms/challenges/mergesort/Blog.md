# Merge Sort
### Merge sort is a method by which you break an unsorted array down into two smaller halves and so forth until you have a bunch of arrays of only two items. You sort each one, then merge each with another two-item array, then you merge the four-item arrays and so on all the way back up to a fully sorted array.31‏/01‏/2017

### Pseudocode
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

# Trace

### Sample Array: [8,2,7,3]

## pass1:
###   left =[8,2]  , right = [7,3]
### split the array in two picas and save each one of them in variable

## pass2 :
###   array = [8,2]  ,  left =[8] , right =[2]
### split the main left into left and right

## pass3 :
### array = [2,8]
### merge the left and right and put them in sorted way

## pass4 :
###   array = [7,3]  ,  left =[7] , right =[3]
#### split the mainright  into left and right

## pass5 :
### array = [3,7]
### merge the left and right and put them in sorted way

## pass6:
### array = [2,3,7,8]
### ake the last sorted left and merge it with the last sorted right  to have the array in sorted way


# Efficency
- Time: O(n*log n)

- Space: O(1)



