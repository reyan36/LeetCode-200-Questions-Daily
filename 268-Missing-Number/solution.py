class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        result = n * (n+1) // 2
        return result-sum(nums)
         