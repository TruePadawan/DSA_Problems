from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        iterator = head
        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    iterator.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    iterator.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1 is not None:
                iterator.next = ListNode(list1.val)
                list1 = list1.next
            else:
                iterator.next = ListNode(list2.val)
                list2 = list2.next
            iterator = iterator.next
        return head
