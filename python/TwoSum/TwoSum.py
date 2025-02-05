from typing import List
nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in dic and dic[complement] != i:
                return [dic[complement],i]
            dic[nums[i]] = i
        return []

print(Solution().twoSum(nums, target))