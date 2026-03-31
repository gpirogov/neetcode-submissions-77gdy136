# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        # EC: len(list) = 1 and there's NO cycle
        # EC: len(list) = 1 and there's a cycle
        # EC: len(list) > 1 and the cycle is on the final node

        # optimal solution: turtle and the hare

        

        # EC: len(list) = 0
        if head == None: return False

        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: return True

        return False
