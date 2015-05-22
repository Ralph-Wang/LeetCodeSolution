# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        h = head
        pre = None
        while h is not None:
            if h.val == val:
                print 'hit'
                if pre is None:
                    head = h.next
                    pre = None
                else:
                    pre.next = h.next
            else:
                pre = h
            h = h.next
        return head




head = ListNode(1)
h = head
for i in [2,2,1]:
    h.next = ListNode(i)
    h = h.next

h = head

while h is not None:
    print h.val
    h = h.next

print '-' * 20

s = Solution()
h = s.removeElements(head, 2)

print '-' * 20

while h is not None:
    print h.val
    h = h.next
