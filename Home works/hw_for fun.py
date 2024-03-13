# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,7,11,15]
target = 9
# len(nums)
# range(nums[0], nums[-1]) # принтит от 2 до 14 численно
for x in nums:
    for y in nums:
        if y == target - x:
            print(f' {x} + {y} = {target}', '\n', nums.index(x), nums.index(y))
            break

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
        
# nums = [3,2,4]
# target = 6
        
# for x in nums:
#     for y in nums:
#         if y == target - x:
#             print([nums.index(x), nums.index(y)])
#             break

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# nums = [3,3]
# target = 6
# for x in nums:
#     for y in nums:
#         if y == target - x:
#             print(f' {x} + {y} = {target}', '\n', nums.index(x), nums.index(y))
#             break