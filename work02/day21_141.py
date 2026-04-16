# ============================================
# @File    : day21_141.py
# @Date    : 2026-04-12 16:27
# @Author  : 帅宇昕
# ============================================
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     '''
    #     hash表的做法
    #     :param head:
    #     :return:
    #     '''
    #     # 创建集合
    #     linkSet=set()
    #     # 然后一直循环，看下一个数据是不是在里面
    #     if head is None:
    #         return False
    #
    #     p=head
    #     while p is not None:
    #         if p in linkSet:
    #             return True
    #         linkSet.add(p)
    #         p=p.next
    #     return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False
        # 快慢指针
        s = head
        f = head.next
        while s!=None and f!=None:
            if s==f:
                return True
            s=s.next

            f=f.next
            if f ==None:
                return False
            f=f.next
        return False