'''
This is all the classes that are used for local debugging of the ListNode related problems in LeetCode. 
'''

# define ListNode
class ListNode:
    '''
    Class of ListNode in Leetcode. 

    Args:
        val: Value of the node
        next: pointer to the next ListNode
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# define SingleLink
class SingleLink:
    '''
    Class of a single link made of class ListNode

    Arg:
        ls: list to be converted into SingleLink
    '''
    def __init__(self, ls: list) -> None:
        self.ls = ls
    
    def listToListNode(self):
        '''
        Function to convert list to SingleLink

        return:
            ptr: pointer to the first ListNode of the SingleLink
        '''
        dummy = ListNode(0)
        ptr = dummy
        for num in self.ls:
            ptr.next = ListNode(num)
            ptr = ptr.next
        
        ptr = dummy.next
        return ptr

class ListNodePrinter:
    '''
    Class of a printer of a SingleLink

    Args:
        node: first ListNode of the SingleLink
    '''
    @staticmethod
    def print_ListNode(node: ListNode) -> None:
        '''
        printing the SingleLink
        '''
        ls = []
        while node:
            ls.append(node.val)
            node = node.next
        print(ls)