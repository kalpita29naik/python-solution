class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        count = len(words)
        word_len = len(words[count-1])
        return word_len
        
