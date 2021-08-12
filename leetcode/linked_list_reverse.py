class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        

def main(list_node: ListNode):
    head = list_node
    next = None
    temp = None
    while head:
        next = head.next
        head.next = temp
        temp = head
        head = next
        
    
    return head

if __name__ == '__main__':
    main(ListNode(12, ListNode(5, ListNode(2))))
    