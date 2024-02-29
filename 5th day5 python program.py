def min_jumps_to_end(nums):
    if not nums:
        return -1

    n = len(nums)
    jumps = 0
    max_reach = 0
    curr_end = 0

    for i in range(n - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == curr_end:
            jumps += 1
            curr_end = max_reach

            if curr_end >= n - 1:
                return jumps

        if i == max_reach:
            return -1

    return jumps if curr_end >= n - 1 else -1

# Test cases
print(min_jumps_to_end([2, 3, 1, 1, 4]))  # Output: 2 (Jump from index 0 to 1, then from index 1 to 4)
print(min_jumps_to_end([3, 2, 1, 0, 4]))  # Output: -1 (Cannot reach the end)
