class Solution:
    def countDigits(self, num: int) -> int:
        count = 0 

        for d in str(num):
            digit = int(d)
            if num % digit == 0 and digit != 0: 
                count += 1
        return count