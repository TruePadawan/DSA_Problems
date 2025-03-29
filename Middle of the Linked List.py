# Definition for singly-linked list.
import math
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Loop through the linked-list and add form a list
get the length of the list
divide by 2 - floor it
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        normal_list = []
        while (head is not None):
            normal_list.append(head)
            head = head.next
        middle_index = math.floor(len(normal_list)/2)
        return normal_list[middle_index]