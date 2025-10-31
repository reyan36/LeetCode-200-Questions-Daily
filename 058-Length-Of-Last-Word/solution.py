class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordsss = s.split()
        return len(wordsss[-1])
