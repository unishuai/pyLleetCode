# ============================================
# @File    : day25_19.py
# @Date    : 2026-04-13 9:25
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #遍历一遍，然后知道节点长度，顺便可以知道倒数第N个节点

        #用列表存储每一个节点的pre和p的节点指针，然后倒数可以直接找到

        #这里可以用双链表的方式，第二个链表在第一个链表的前面
        pass
