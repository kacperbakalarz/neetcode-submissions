class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        if len(s1) > len(s2):
            return False
        
        hash_map = [0 for _ in range(26)]
        hash_map2 = [0 for _ in range(26)]

        for letter in s1:
            hash_map[ord(letter)-97] += 1
        
        start = 0
        end = len(s1)
        for i in range(start,end):
            hash_map2[ord(s2[i])-97] += 1
        if hash_map2 == hash_map:
                return True 
        while end < len(s2):
            hash_map2[ord(s2[start])-97] -= 1
            hash_map2[ord(s2[end])-97] += 1
            if hash_map2 == hash_map:
                return True 
            end += 1
            start += 1
           
        
        return False