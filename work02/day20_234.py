# ============================================
# @File    : day20_234.py
# @Date    : 2026-04-11 21:41
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #判断回文
        #先循环一遍，知道它的长度，然后第二遍
        #第二遍，在中间的位置开始回文，左边的是逆序走，右边正常走
        if head==None or head.next==None:
            return True

        linkLen=0
        p=head
        while p !=None:
            linkLen+=1
            p=p.next
        #判断奇数还是偶数
        left = linkLen // 2


        count=0
        pre=None
        p = head
        q = p.next
        while count<left:
            q=p.next
            p.next=pre
            pre=p
            p=q
            count+=1


        if linkLen % 2 == 0:

            rp=p
        else:

            rp = p.next

        while rp!=None and pre!=None:
            if rp.val!=pre.val:
                return False
            rp=rp.next
            pre=pre.next
        return True


    #



