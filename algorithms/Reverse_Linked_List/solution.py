# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        pre = None
        while head is not None:
            cur = head
            head = head.next
            assert head is cur.next
            cur.next = pre
            pre = cur
        return pre


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()

head = s.reverseList(head)


while head is not None:
    print head.val
    head = head.next
