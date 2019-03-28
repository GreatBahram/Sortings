# Bubble Sort
A bubble sort algorithm iterates through the list or array that it is given, and compares each pair of adjacent elements in the list by size. If they elements are in the incorrect order, it swaps them, and then moves on to the next pair of elements.

* After x iterations, checking the last x elements in a collection is redundant. (This is that we decrease length variable in our code, after each iteration.)

## How does it work?

```python
>>> from selection import bubble_sort
>>>
>>> unsorted_list = [33,2,52,106,73]
>>>
>>> sorted_list = bubble_sort(unsorted_list)
>>> print(sorted_list)
[2, 33, 52, 73, 106]
```
## Conclusion
* Time complexity: O(n²)
* Space complexity: In-place
* Stability: Stable
* Internal/External: Internal
* Recursion/Non-Recursion: Non-recursion
