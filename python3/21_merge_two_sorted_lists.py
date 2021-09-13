from list_to_listnode import ListNode, SingleLink, ListNodePrinter

class Solution:
    def mergeTwoLists(self, l1, l2):
        output = ListNode()
        tail = output
        while l1 and l2:
            if l1.val>=l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return output.next

if __name__=="__main__":
    # input
    l1 = [1, 1, 2]
    l2 = [1, 3, 4]

    # convert lists to SingleLink
    link1 = SingleLink(l1)
    link2 = SingleLink(l2)

    # calculate the merged list
    solution = Solution()
    ptr = solution.mergeTwoLists(link1.listToListNode(), link2.listToListNode())

    # print the merged list
    ListNodePrinter.print_ListNode(ptr)