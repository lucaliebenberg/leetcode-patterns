# Next greater element - Stack example

def next_greater_element(arr):
    n = len(str)
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
            
        stack.append()

    return result
