class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast = slow = nums[0]

        #  Checking for the cycle 
        while True:
            fast = nums[nums[fast]] # Two Times
            slow = nums[slow] # One Times

            if slow == fast: 
                break

        # Taking out the value
        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow] 

        return slow