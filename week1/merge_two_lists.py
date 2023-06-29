from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None: return l2
    if l2 is None: return l1
    if l1.val <= l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    if l1.val >= l2.val:
        l2.next = merge_two_lists(l1, l2.next)
        return l2

def ListNode_to_list(l1):
    l2 = []
    if l1 is None:
        return l2
    while l1:
        l2.append(l1.val)
        l1 = l1.next
    return l2

assert ListNode_to_list(None) == []
assert ListNode_to_list(ListNode(val=1, next=ListNode(val=2))) == [1,2]

print("Passed all the tests for ListNode_to_list 🎉")