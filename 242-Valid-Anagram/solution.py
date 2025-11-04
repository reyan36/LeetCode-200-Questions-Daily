class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = {}
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1

        dict_t = {}
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        return dict_s == dict_t