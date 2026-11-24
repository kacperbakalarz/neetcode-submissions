# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0 
        count = 1 
        count2 = 1
        while l1:
            num1 += count*l1.val
            l1 = l1.next
            count *= 10

        while l2:
            num2 += count2*l2.val
            l2 = l2.next
            count2 *= 10

        num3 = num1+num2
        #print(num3)
        count3 = 1
        dummy = ListNode()
        l3 = dummy
        if num3 == 0:
            return ListNode(0)
        while num3 > 0:
            char = num3%10
            l3.next = ListNode(char)
            l3 = l3.next
            num3 //= 10

        return dummy.next


            