# ============================================
# @File    : day18_160.py
# @Date    : 2026-04-11 14:53
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     # 我的思路是，先循环一遍，找到每一个的末端点
    #     # 如果末端点是一致的话，就说明存在值,然后在反推
    #     # 不一致就输出 No intersection
    #     linkA=headA
    #     listA=[]
    #     while linkA.next is not  None:
    #         listA.append(linkA)
    #         linkA=linkA.next
    #     listA.append(linkA)
    #
    #     linkB=headB
    #     listB = []
    #     while linkB.next is not  None:
    #         listB.append(linkB)
    #         linkB=linkB.next
    #     listB.append(linkB)
    #     blen=len(listB)
    #     alen=len(listA)
    #     minLen=min(blen,alen)
    #     resId=None
    #     isMatch=False
    #     for i in range(minLen):
    #         if listA[alen-i-1] == listB[blen-i-1]:
    #             isMatch=True
    #             resId=listA[alen-i-1]
    #         else:
    #             break
    #     if isMatch:
    #         return resId
    #     return resId

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     #使用哈希表
    #     listA=set()
    #     linkA=headA
    #     while linkA.next is not None:
    #         listA.add(linkA)
    #         linkA=linkA.next
    #     listA.add(linkA)
    #     linkB = headB
    #     while linkB.next is not None:
    #         if linkB in listA:
    #             return linkB
    #         linkB=linkB.next
    #     if linkB in listA:
    #         return linkB
    #     return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        linkA=headA
        linkB=headB
        #     while linkA.next is not None:
        #         listA.add(linkA)
        #         linkA=linkA.next


