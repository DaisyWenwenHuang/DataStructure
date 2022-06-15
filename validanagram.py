# https://leetcode.com/problems/valid-anagram/
# hashtable
# anagram: a word of phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashtable = {}
        for char in s:
            if char in hashtable:
                hashtable[char] += 1
            else:
                hashtable.get(char,0)
        for ele in t:
            