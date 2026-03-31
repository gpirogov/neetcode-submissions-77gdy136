# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n!) solution would be to loop through it on repeat.
        # O(n) solution is to use a hash-set, but that is O(n) space complexity...
        # O(n) time, O(1) space is i guess just to go thru it twice. O(2n) then, but whatever.
        # ^ NVM that is wrong. i can just use multiple pointers and reset .next's

        if head == None or head.next == None: return head
        prevNode = head
        curNode = head.next
        nextNode = head.next # arbitrary assignment
        prevNode.next = None # creates new tail

        # find 
        while nextNode != None:
            nextNode = curNode.next

            curNode.next = prevNode
            if nextNode == None: break
            prevNode = curNode 
            curNode = nextNode
        return curNode

