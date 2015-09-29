# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    @staticmethod
    def advance_twice(head):
        next = head.next
        if next is not None:
            next = next.next
        return next

    @staticmethod
    def advance_once(head):
        next = head.next
        return next

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # visited
        # visited = set()
        # while head is not None and head not in visited:
        #     visited.add(head)
        #     head = head.next
        # return head

        # two pointer
        fast = head
        slow = head

        while fast is not None and slow is not None:
            fast = self.advance_twice(fast)
            slow = self.advance_once(slow)

            if fast is None:
                return None

            if fast == slow: # make lA, lB to have same length
                fast = head
                while fast != slow:
                    fast = self.advance_once(fast)
                    slow = self.advance_once(slow)
                return slow
        return None
