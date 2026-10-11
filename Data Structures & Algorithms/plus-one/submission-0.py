class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mnoznik = 1
        liczba = 1
        for i in range(len(digits)-1,-1,-1):
            liczba += digits[i]*mnoznik
            mnoznik*=10
        ans = []
        while liczba > 0:
            ans.append(liczba%10)
            liczba //=10
        return ans[::-1]