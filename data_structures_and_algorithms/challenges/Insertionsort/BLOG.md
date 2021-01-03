## Pseudocode
```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```
## Trace

- [7,0,3]
#### pass1
1.  min=0 , i = 0 , temp = 7
- [7,0,3]-->[0,7,3]
### In the first pass through of the selection sort, we evaluate if there is a smaller number in the array than what is currently present in index 0. We find this smaller number right away in index 1. The minimum value gets updated to remember this index. At the end of the evaluation, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first.

#### pass2
2. min=1 , i = 1, temp = 0
- [0,7,3]-->[0,3,7]
### The 2th pass through of the array only has one other index to evaluate. Since the last index value is larger than index 2, the two values will swap.


#### pass3
3. min=2 , i = 2, temp = 3
- [0,3,7]-->[0,3,7]
### On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself.
## Efficency
- Time: O(n^2)
- Space: O(1)






