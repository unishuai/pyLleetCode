# ============================================
# @File    : day22_142.py
# @Date    : 2026-04-12 17:31
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #用集合会更方便一点
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # zeroNode=ListNode(0)
        if head == None:
            return None
        q = head
        s=head
        f=head.next
        count = 0
        while f!=None:
            if s is f:
                s=s.next
                while q != s:
                    q=q.next
                    s=s.next
                return q
            s=s.next
            f=f.next
            if f is None:
                return None
            f=f.next
        return None



