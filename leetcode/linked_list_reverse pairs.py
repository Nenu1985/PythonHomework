from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    result = ListNode()
    def swap(self, head: Optional[ListNode])-> Optional[ListNode]:

        if not head:
            return
    
        next = head.next  # 2
        
        next_next = head.next.next  # 3

        next.next = head  # 2 links to 1 rather than 3
        head.next = next_next  # # 1 links to 3 rather than 2
        next.next.next = self.swap(next.next.next)
        return next
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''''''
        # result_list = ListNode(head)
        
        return self.swap(head)


if __name__ == '__main__':
    s = Solution()
    result_list = s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

    