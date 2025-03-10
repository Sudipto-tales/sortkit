from .exception_handler import exception_handler

@exception_handler
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def choose_algo(arr):
    n = len(arr)
    
    if is_sorted(arr):
        print("Insertion Sort")
    
    elif n <= 20:
        print("Insertion Sort")
    
    elif 20 < n <= 1000:
        unique_elements = len(set(arr))
        
        if unique_elements <= n // 2:
            print("Merge Sort")
        
        elif all(isinstance(x, int) for x in arr):
            min_val, max_val = min(arr), max(arr)
            if max_val - min_val < 10_000:
                print("Counting Sort")
            else:
                print("Quick Sort")
        
        else:
            print("Quick Sort")

    elif n > 1000:
        unique_elements = len(set(arr))

        if unique_elements <= n // 10:
            print("Radix Sort")
        
        elif all(isinstance(x, str) for x in arr):
            print("Radix Sort or Merge Sort")
        
        elif n > 10_000:
            print("Heap Sort")

        else:
            print("Quick Sort")

