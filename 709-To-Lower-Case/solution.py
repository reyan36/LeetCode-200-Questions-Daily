class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for value in s:
            if 'A'<= value <= 'Z':
                result += chr(ord(value) + 32)
            else:
                result += value
        return result
