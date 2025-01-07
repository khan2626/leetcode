class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'{self.val}-->{self.next}'

def merge_two_sorted_list(list1, list2):

    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
    return dummy.next

def to_linked_list(lst):
    dummy = ListNode()
    curr = dummy

    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == '__main__':
    list1 = to_linked_list([1, 2, 4])
    list2 = to_linked_list([1, 2, 3])
    print(merge_two_sorted_list(list1, list2))
            
            