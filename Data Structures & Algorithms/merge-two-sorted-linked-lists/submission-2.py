# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if curr1.val <= curr2.val:
            ans = curr1

            curr1 = curr1.next
        else:
            ans = curr2

            curr2 = curr2.next
        head = ListNode()
        head.next = ans 
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                ans.next = curr1
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                ans.next = curr2
                curr2 = curr2.next

            ans = ans.next
        
        if curr1 is None:
                ans.next = curr2
        else:
                ans.next = curr1
                
        return head.next

        