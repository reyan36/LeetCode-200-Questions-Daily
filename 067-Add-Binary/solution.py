class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first_str = int(a, 2)
        second_str = int(b, 2)

        res = first_str + second_str 

        new_binary = bin(res)
        return new_binary.replace('0b', '', 1)