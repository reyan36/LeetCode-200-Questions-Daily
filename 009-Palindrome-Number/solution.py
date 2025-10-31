class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        rev_num = 0
        original_num = x

        while original_num > 0:
            rev_num = rev_num * 10 + original_num % 10
            original_num //= 10
        
        if (rev_num == x):
            return True
        else:
            return False