def smallerNumbersThanCurrent(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    sorted_nums = sorted(counts.keys())
    result = []
    for num in nums:
        smaller_count = sum(counts[sorted_num] for sorted_num in sorted_nums if sorted_num < num)
        result.append(smaller_count)
    
    return result

# Test case
nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))  # Output: [4, 0, 1, 1, 3]
