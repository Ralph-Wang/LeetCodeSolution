# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # # visited
        # visited = set()
        # while headA is not None:
        #     visited.add(headA)
        #     headA = headA.next

        # while headB is not None:
        #     if headB in visited:
        #         return headB
        #     headB = headB.next
        # return None

        # merge list
        if not headA or not headB:
            return None
        ptA, ptB, jumpA, jumpB = headA, headB, False, False
        while True:
            if ptA is ptB:
                return ptA
            ptA, ptB = ptA.next, ptB.next
            if not ptA:
                if not jumpA:
                    jumpA = True
                    ptA = headB
                else:
                    return None
            if not ptB:
                if not jumpB:
                    jumpB = True
                    ptB = headA
                else:
                    return None


        # # same length
        # lA = self.get_len(headA)
        # lB = self.get_len(headB)

        # while lA != lB: # ensure A/B have same length
        #     if lA < lB:
        #         headB = headB.next
        #         lB -= 1
        #     else:
        #         headA = headA.next
        #         lA -= 1

        # while headA != headB:
        #     headA = headA.next
        #     headB = headB.next
        # return headA

    # @staticmethod
    # def get_len(node):
        # l = 0
        # while node is not None:
        #     l += 1
        #     node = node.next
        # return l

