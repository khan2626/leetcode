
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'
    
def toLinkedList(lst):
    dummy = ListNode()
    curr = dummy
    
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


if __name__ == '__main__':
    print(toLinkedList(lst=[1,2,3,4,5]))
