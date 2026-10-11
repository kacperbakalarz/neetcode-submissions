class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            letters = []
            for letter in string: 
                letters.append(letter)
            letters = sorted(letters)
            letters = tuple(letters)

            if letters in hash_map:
                hash_map[letters].append(string)
            else:
                hash_map[letters] = [string]
        
        ans = []
        
        for tab in hash_map:
            ans.append(hash_map[tab])
        #print(hash_map)
        return ans 
            
