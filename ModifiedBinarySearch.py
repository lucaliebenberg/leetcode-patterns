
# Use Case questions:
## Searching in a nearly sorted array
## Searching in a rotated sorted array
## Searching in a list with unknown length
## Searching in an array with duplicates
## Finding the first or the last occurence of an element
## Finding the square root of a number
## Finding a peak element


# Search Rotated Array example

def search_sorted_array(nums, target):
    left, right  0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
