def create_prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr
