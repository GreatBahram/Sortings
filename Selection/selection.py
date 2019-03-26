def selection_sort(iterator):
    """
    Here’s what our Selection sort algorithm might look like, in Python3:
    """
    for index, item in enumerate(iterator):
        smallest_item = min(iterator[index:])
        smallest_index = iterator[index:].index(smallest_item)

        if smallest_item < item:
            iterator[index] = smallest_item
            iterator[index + smallest_index] = item 
    return iterator
