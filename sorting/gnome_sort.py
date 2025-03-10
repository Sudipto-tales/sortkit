from sorting.exception_handler import exception_handler

@exception_handler
def recursive_gnome_sort(arr, index=0):
    """Sorts the array using recursive Gnome Sort algorithm."""
    if index >= len(arr):
        return arr  # Base case: If index exceeds array length, sorting is done

    if index == 0 or arr[index] >= arr[index - 1]:
        return recursive_gnome_sort(arr, index + 1)  # Move forward
    else:
        arr[index], arr[index - 1] = arr[index - 1], arr[index]  # Swap
        return recursive_gnome_sort(arr, index - 1)  # Move back

