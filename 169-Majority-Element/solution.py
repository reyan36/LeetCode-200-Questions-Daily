class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        target_count = len(nums) // 2

        for value in nums:
            if value in freq:
                freq[value] += 1
            else:
                freq[value] = 1 

            if freq[value] > target_count:
                return value