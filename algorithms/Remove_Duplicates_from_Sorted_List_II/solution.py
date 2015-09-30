# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        cur = head
        pre = None
        dup = False
        while cur is not None:
            next = cur.next
            if next is None or next.val != cur.val:
                if dup and pre is None:
                    head = next
                    dup = False
                elif dup and pre is not None:
                    pre.next = next
                    dup = False
                else:
                    pre = cur
            if next is not None and next.val == cur.val:
                dup = True

            cur = next
        return head


head = ListNode(0)

h = head

for i in xrange(1, 5):
    if i == 3 or i == 1:
        h.next = ListNode(i)
        h = h.next
    h.next = ListNode(i)
    h = h.next

h = head
while h is not None:
    print h.val,
    h = h.next
print
s = Solution()
head = s.deleteDuplicates(head)


h = head
while h is not None:
    print h.val,
    h = h.next
