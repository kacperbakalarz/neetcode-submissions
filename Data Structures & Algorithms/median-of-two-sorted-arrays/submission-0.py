class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = []
        for num in nums1:
            num3.append(num)
        for num in nums2:
            num3.append(num)
        num3.sort()
        if len(num3) % 2 != 0:
            return num3[len(num3)//2]
        else:
            #print(num3[len(num3)//2])
            #print(num3[len(num3)//2-1])
            return (num3[len(num3)//2]+num3[len(num3)//2-1])/2