# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curL1Node = list1
        curL2Node = list2
        curMergedNode = ListNode()
        mergedHead = None

        # if mergedHead == None: print("test")

        if curL1Node is not None or curL2Node is not None:
            if curL2Node is None:
                return curL1Node
            elif curL1Node is None:
                return curL2Node
            elif curL1Node.val > curL2Node.val:
                curMergedNode = mergedHead = curL2Node
                curL2Node = curL2Node.next
            else:
                curMergedNode = mergedHead = curL1Node
                curL1Node = curL1Node.next


        while curL1Node is not None or curL2Node is not None: 

            if curL2Node is None:
                if mergedHead is None: 
                    curMergedNode = mergedHead = curL1Node
                else:
                    curMergedNode.next = curL1Node
                break

            elif curL1Node is None:
                if mergedHead is None: 
                    curMergedNode = mergedHead = curL2Node
                else:
                    curMergedNode.next = curL2Node
                break

            else:
                if curL1Node.val > curL2Node.val:
                    if mergedHead is None: 
                        curMergedNode = mergedHead = curL2Node
                    else:
                        curMergedNode.next = curL2Node
                        curMergedNode = curMergedNode.next
                    curL2Node = curL2Node.next
                else:
                    if mergedHead is None: 
                        curMergedNode = mergedHead = curL1Node
                    else:
                        curMergedNode.next = curL1Node
                        curMergedNode = curMergedNode.next
                    curL1Node = curL1Node.next

        return mergedHead
