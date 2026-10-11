class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 = {}
        hash_2 = {}
        if len(s) != len(t):
            return False 
        for i in range(len(s)):
            if s[i] not in hash_1:
                hash_1[s[i]] = 1
            else:
                hash_1[s[i]] += 1
            
            if t[i] not in hash_2:
                hash_2[t[i]] = 1
            else:
                hash_2[t[i]] += 1
        
        return hash_1 == hash_2
        