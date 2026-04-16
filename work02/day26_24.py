# ============================================
# @File    : day26_24.py
# @Date    : 2026-04-13 10:02
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head ==None or head.next==None:
    #         return head
    #     #两个节点一样
    #
    #     pre=ListNode()
    #     pre.next=head
    #     newhead=pre
    #     p=head
    #     q=head.next
    #     while q !=None:
    #         p.next=q.next
    #         q.next=p
    #         pre.next=q
    #         q=p
    #
    #         #判断是否能前进两位
    #         if q.next ==None or q.next.next ==None:
    #             return newhead.next
    #
    #         pre=q
    #         p=q.next
    #         q=q.next.next
    #     return pre.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #如果是递归的写法的话
        if head ==None or head.next==None:
            return head
        #他们会变化
        newHead=head.next
        head.next=self.swapPairs(newHead.next)
        newHead.next=head
        return newHead


