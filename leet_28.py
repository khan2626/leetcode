
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'
    
def to_linked_list(lst):
    dummy = ListNode()
    curr = dummy

    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next
    
def removeNthFromEnd(head, n):
    fast = head
    slow = head

    for i in range(n):
        fast = fast.next

    if not fast:
        return head.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head
if __name__ == '__main__':
    lst = to_linked_list([1,2,3,4,5])
    print(removeNthFromEnd(lst, 2))

    
    
