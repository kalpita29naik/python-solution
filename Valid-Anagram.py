class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets = "".join(sorted(s))
        sett = "".join(sorted(t))
        if sets == sett:
            return True
        else:
            return False
        
