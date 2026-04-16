# ============================================
# @File    : day23_21.py
# @Date    : 2026-04-12 20:18
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2
        head=ListNode(0)
        p=head
        q=None
        while p1!=None and p2 != None:
            if p1.val <p2.val:
                q=p1
                p1=p1.next

            else:
                q = p2
                p2 = p2.next

            p.next = q
            p = p.next
            p.next = None
        if p1 !=None:
            p.next=p1
        elif p2 !=None:
            p.next = p2
        return head.next



