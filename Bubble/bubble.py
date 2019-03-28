def bubble_sort(iterator):
    """
    Here’s what our Bubble sort algorithm might look like, in Python3:
    """
    length = len(iterator) -1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if iterator[i] > iterator[i+1]:
                is_sorted = False
                iterator[i], iterator[i+1] = iterator[i+1], iterator[i]
        length -= 1
    return iterator
