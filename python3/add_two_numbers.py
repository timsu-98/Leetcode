# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Time: O(N)
    Space: O(1)
    runtime 167 ms
    memory usage 14.1 MB
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            #update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

class Solution_2:
    '''
    Time: O(N)
    Space: O(1)
    runtime 80 ms
    memory usage 14.2 MB
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            carry, val = divmod(v1 + v2 +carry, 10)
            cur.next = ListNode(val)

            #update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next