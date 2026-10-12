class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        letters = {}
        i = 0
        j =1
        letters[s[i]] = 1
        maxi = 1
        
        while j < len(s):
            if s[j] in letters:
                letters[s[j]] += 1
                while letters[s[j]] == 2:
                    letters[s[i]] -= 1
                    i += 1
            else:
                letters[s[j]] = 1
            maxi = max(j-i+1,maxi)
            j +=1

        return maxi