# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curL1Node = list1
        curL2Node = list2
        mergedHead = curMergedNode = ListNode()

        while curL1Node is not None and curL2Node is not None:
            '''if curL2Node is None: return curL1Node
            if curL1Node is None: return curL2Node
            if curL1Node.val > curL2Node.val:
                curMergedNode = mergedHead = curL2Node
                curL2Node = curL2Node.next
            else:
                curMergedNode = mergedHead = curL1Node
                curL1Node = curL1Node.next'''


            # while True: 
            '''if curL2Node is None:
                curMergedNode.next = curL1Node
                break
            if curL1Node is None:
                curMergedNode.next = curL2Node
                break'''
            
            if curL1Node.val > curL2Node.val:
                curMergedNode.next = curL2Node
                curL2Node = curL2Node.next
            else:
                curMergedNode.next = curL1Node
                curL1Node = curL1Node.next

            curMergedNode = curMergedNode.next

        curMergedNode.next = curL1Node or curL2Node

        return mergedHead.next