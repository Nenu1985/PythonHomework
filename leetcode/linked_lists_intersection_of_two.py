# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def if_val_exists(self, val: int, node_type: str, count: int):
        if val in self.hash_nodes and self.hash_nodes[val][0] != node_type:
            self.intersection_val = val
            self.hash_nodes[val] = { 
                                    self.hash_nodes[val][0]: self.hash_nodes[val][1],
                                    node_type: count
            }
            return True
        self.hash_nodes[val] = (node_type, count)
        return False

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_head_a = headA
        cur_head_b = headB
        
        len_a = 0
        while cur_head_a:
            len_a += 1
            cur_head_a = cur_head_a.next
            
        while cur_head_a:
            len_a += 1
            cur_head_a = cur_head_a.next
            
            
        return result_node

    def stringToListNode(self,number_string: List[int]):
            previousNode = None
            first = None
            for i in number_string:
                currentNode = ListNode(i)
                if first is None:
                    first = currentNode
                if previousNode is not None:
                    previousNode.next = currentNode
                previousNode = currentNode
            return first

if __name__ == '__main__':
    s = Solution()
    l1 = s.stringToListNode([1,9,1,2,4])
    l2 = s.stringToListNode([3,2,4])
    
    l1 = s.stringToListNode([4,1,8,5,5])
    l2 = s.stringToListNode([5,6,1,8,4,5])
    s.getIntersectionNode(l1, l2)