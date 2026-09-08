class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        tdic = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in sdic:
                sdic[s[i]] = 1
            else:    
                sdic[s[i]]+=1
            if t[i] not in tdic:
                tdic[t[i]] = 1
            else:    
                tdic[t[i]]+=1
        if sdic != tdic:
            return False
        else:
            return True
            
            