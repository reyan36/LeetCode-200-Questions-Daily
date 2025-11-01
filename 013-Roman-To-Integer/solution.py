class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum_1 = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n - 1 and roman_list[s[i]] < roman_list[s[i+1]]:
                sum_1 += roman_list[s[i+1]] - roman_list[s[i]]
                i += 2
            else:
                sum_1 += roman_list[s[i]]
                i += 1
        return sum_1     
        