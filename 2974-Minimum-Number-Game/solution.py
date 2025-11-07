class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()  
        nums[::2], nums[1::2] = nums[1::2], nums[::2]  
        arr = nums[:]  
        return arr
