class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in t:
            freq[char] = freq.get(char, 0) - 1

        # If all counts return to zero, it's an anagram
        return all(value == 0 for value in freq.values())
