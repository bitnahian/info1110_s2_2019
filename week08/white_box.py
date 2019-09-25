def my_max(nums):
    # Check for nums type
    if not isinstance(nums, list):
        return -1
    
    for num in nums:
        if not isinstance(num, int):
            return -1


    # Check for empty list
    if len(nums) == 0:
        return -1

    maximum = 0
    i = 0
    while i < len(nums):
        if nums[i] > nums[maximum]:
            maximum = i
        i += 1
    return maximum

