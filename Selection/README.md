# Selection Sort
A selection sort algorithm sorts through a list of items by iterating through a list of elements, finding the smallest one, and putting it aside into a sorted list. It continues to sort by finding the smallest unsorted element, and adding it to the sorted list.

A selection sort algorithm will swap the smallest element it finds in each iteration, and add it to the sorted section of elements.


## How does it work?
    1. We traverse through all the elements in the number array.
    1. We set the current item to be the smallest/minimum.
    1. If the next number is smaller than the current number, we reassign our reference to the the index of the smallest number.
    1. If the number we’re looking at is the smallest in size, we swap it with the first element.

```python
>>> from selection import selection_sort
>>>
>>> unsorted_list = [33,2,52,106,73]
>>>
>>> sorted_list = selection_sort(unsorted_list)
>>> print(sorted_list)
[2, 33, 52, 73, 106]
```
## Conclusion
* Time complexity: O(n²)
* Space complexity: In-place
* Stability: Unstable
* Internal/External: Internal
* Recursion/Non-Recursion: Non-recursion
