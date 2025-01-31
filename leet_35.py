"""
class ListNode
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'
    
def toLinkedList(lst):
    """
    It converts an array to a linked list
    """
    dummy = ListNode()
    curr = dummy
    
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

"""
It rotate the linked list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""

def rotateList(head, k):
    if not head:
        return head
    
    length, tail = 1, head
    while tail.next != None:
        tail = tail.next
        length +=1

    k = k % length
    if k == length or k == 0:
        return head
    
    curr = head
    for i in range(length - k - 1):
        curr = curr.next
    newHead = curr.next
    curr.next = None
    tail.next = head
    return newHead


if __name__ == '__main__':
    ll = toLinkedList(lst=[1,2,3,4,5])
    print(rotateList(ll, k=2))
