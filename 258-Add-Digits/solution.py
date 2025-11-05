class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        digital_root = 1+(num-1)%9
        return digital_root
