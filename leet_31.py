

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'
    
def to_linked_lst(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def swap_pairs(head):
    dummy = ListNode(0)
    prev = dummy

    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        prev.next = tmp
        prev = tmp.next
        head = head.next
    return dummy.next

if __name__ == '__main__':
    lst = to_linked_lst([1,2,3,4])
    print(swap_pairs(lst))