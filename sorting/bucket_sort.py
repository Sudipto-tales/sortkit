from sorting.exception_handler import exception_handler

@exception_handler
def bucket_sort(arr):
    """Sorts the array using Bucket Sort."""
    if not arr:
        return arr

    bucket_count = len(arr)
    max_val, min_val = max(arr), min(arr)
    bucket_range = (max_val - min_val) / bucket_count
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        index = min(index, bucket_count - 1)  # Ensure index is within range
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()  # You can use any sorting algorithm here

    return [num for bucket in buckets for num in bucket]  # Flatten buckets
