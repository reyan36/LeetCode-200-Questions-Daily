class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup_bag = {}

        for i , num in enumerate(nums):
            x = target - num
            if x in lookup_bag:
                return [lookup_bag[x], i]

            lookup_bag[num] = i