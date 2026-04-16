# ============================================
# @File    : day24_12.py
# @Date    : 2026-04-12 21:33
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1=l1
        p2=l2
        resHead=ListNode(0)
        resP= resHead
        c=0
        while p1 !=None and p2 != None:

            if p1.val + p2.val +c>=10:
                tmpVal=p1.val + p2.val+c-10
                c = 1

            else:
                tmpVal = p1.val + p2.val + c
                c = 0
            tmpNode = ListNode(tmpVal)
            resP.next = tmpNode
            resP = resP.next

            p1=p1.next
            p2=p2.next
        q=None
        if p1 !=None:
            q=p1
        elif p2 !=None:
            q=p2
        while q !=None:
            if q.val+c>=10 :
                tmpVal = q.val + c - 10
                c = 1
            else:
                tmpVal = q.val + c
                c=0

            tmpNode = ListNode(tmpVal)
            resP.next = tmpNode
            resP = resP.next
            q=q.next
        if c==1:
            tmpNode = ListNode(c)
            resP.next = tmpNode
            resP = resP.next

        # print(resHead.val)
        return resHead.next

