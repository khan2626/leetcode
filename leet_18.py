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

def remove_duplicate(head):

    res = head

    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return res

if __name__ == "__main__":
    ll = to_linked_lst([1,1,2,2,3,3])
    print(remove_duplicate(ll))

