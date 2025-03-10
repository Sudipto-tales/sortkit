# This file is part of the 'sorting' package.
# This is used for quick sorting of an array.
# This function is called by the main program to sort the array.
from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort
from .radix_sort import radix_sort
from .heap_sort import heap_sort
from .counting_sort import counting_sort
from .exception_handler import exception_handler

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

@exception_handler
def sorting(arr):
    n = len(arr)
    
    if is_sorted(arr):
        print(arr)
    
    elif n <= 20:
        print(insertion_sort(arr))
    
    elif 20 < n <= 1000:
        unique_elements = len(set(arr))
        
        if unique_elements <= n // 2:
            print(merge_sort(arr))
        
        elif all(isinstance(x, int) for x in arr):
            min_val, max_val = min(arr), max(arr)
            if max_val - min_val < 10_000:
                print(counting_sort(arr))
            else:
                print(quick_sort(arr))
        
        else:
            print(quick_sort(arr))

    elif n > 1000:
        unique_elements = len(set(arr))

        if unique_elements <= n // 10:
            print(radix_sort(arr))
        
        elif all(isinstance(x, str) for x in arr):
            print(merge_sort(arr))
        
        elif n > 10_000:
            print(heap_sort(arr))

        else:
            print(quick_sort(arr))

