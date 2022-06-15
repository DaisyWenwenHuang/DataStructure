# https://leetcode.com/problems/valid-anagram/
# hashtable
# anagram: a word of phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashtableS = {}
        hashtableT = {}
        for i in range(len(t)):
            hashtableS[s[i]] = 1 + hashtableS.get(s[i], 0)
            hashtableT[t[i]] = 1 + hashtableT.get(t[i], 0)
        for char in hashtableT:
            if hashtableT[char] != hashtableS.get(char, 0):
                return False
        return True
        
            