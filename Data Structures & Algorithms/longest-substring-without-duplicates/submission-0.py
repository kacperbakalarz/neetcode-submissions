class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {} 
        i = 0
        j = 0
        ans = 0  # Zmiana z -1 na 0
        
        while j < len(s):
            # 1. Zawsze dodajemy/aktualizujemy aktualny znak s[j]
            if s[j] in dict1:
                dict1[s[j]] += 1
            else:
                dict1[s[j]] = 1
                
            # 2. Jeśli znak w oknie występuje więcej niż raz, kurczymy okno od lewej (i)
            while dict1[s[j]] > 1:
                dict1[s[i]] -= 1
                i += 1
            
            # 3. Liczymy aktualną długość okna (+1 jest tu kluczowe)
            curr = j - i + 1
            ans = max(ans, curr)
            j += 1

        return ans