class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = [0 for _ in range(26)]
        hash2 = [0 for _ in range(26)]
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hash1[ord(s[i])-97] += 1
            hash2[ord(t[i])-97] += 1
        
        #print(hash1,hash2)
        return hash1 == hash2
        