class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers)-1
        suma = numbers[i] + numbers[j]
        while i < j:
            if suma == target:
                return[i+1,j+1]
            elif suma < target:
                i += 1
            else:
                j -= 1
            suma = numbers[i] + numbers[j]
            #print(suma)
        