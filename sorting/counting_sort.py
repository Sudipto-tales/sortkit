from .exception_handler import exception_handler

@exception_handler
def counting_sort(arr, count=None, output=None, index=None):
    if not arr:
        return arr  

    if count is None:
        min_val = min(arr)
        max_val = max(arr)
        range_of_elements = max_val - min_val + 1

        count = [0] * range_of_elements
        output = [0] * len(arr)

        for num in arr:
            count[num - min_val] += 1

        for i in range(1, range_of_elements):
            count[i] += count[i - 1]

        index = len(arr) - 1

    if index < 0:
        return output

    num = arr[index]
    output[count[num - min(arr)] - 1] = num
    count[num - min(arr)] -= 1

    return counting_sort(arr, count, output, index - 1)
