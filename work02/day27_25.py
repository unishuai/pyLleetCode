# ============================================
# @File    : day27_25.py
# @Date    : 2026-04-13 11:29
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        pre=ListNode()
        pre.next=head
        res=pre
        p = head

        queue=list()
        while p!=None:


            for i in range(k):
                if p == None:
                    return res.next
                queue.append(p)
                p=p.next

            for i in range(k):
                tmpp=queue.pop()
                pre.next=tmpp
                pre=pre.next
            pre.next = p

        return res.next


