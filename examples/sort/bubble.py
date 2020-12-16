
def bubble_sort(lst):
    """
    Bubble sort implementation
    Naive s`orting algorithm

    Each of the n items could take n-1 (all other items) comparisons in worst case,
    n * (n-1) = n^2 - n = O(n^2) time complexity performance.

    When we've performed a swap,
    on the next pass i will point to where that element now is,
    meaning that we continue "bubbling" that element up
    for as long as there is an item less than it in front (they are out of order).

    Otherwise, if no swap was performed, i simply moves on to look for an item that
    needs to be swapped.

    When the loop finishes without finding any item that needs to be swapped,
    the whole list must be sorted.
    """
    swapping = True
    while swapping:
        swapping = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swapping = True
                # swap the items
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp


def bubble_sort_optimized(lst):
    
    n = len(lst)

    # for every slot in the list
    for i in range(n):

        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp

    # this works inline, so perhaps returning the list here would be misleading.
    # following the pattern of python's `[].sort` versus `sorted`, don't return anything
