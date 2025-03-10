from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.exception_handler import exception_handler

@exception_handler
def tim_sort(arr):
    """Python Built-in sorted() based on Tim Sort algorithm."""
    RUN = 32  # Default run size for Tim Sort
    n = len(arr)

    # Step 1: Sort small chunks using Insertion Sort
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min((i + RUN - 1), (n - 1)))  # Sorting subarrays

    # Step 2: Merge sorted chunks using Merge Sort
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge_sort(arr, left, mid, right)
        size *= 2  # Double the merge size

    return arr