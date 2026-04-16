# ============================================
# @File    : day19_206.py
# @Date    : 2026-04-11 16:17
# @Author  : 帅宇昕
# ============================================
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head ==None:
    #         return head
    #     #这里可以用到指针
    #     link=head
    #     pre=None
    #     next=None
    #     while link.next!=None:
    #         #下一个链表，头
    #         next=link.next
    #         #指向上一个位置
    #         link.next=pre
    #         #跟新上一个
    #         pre=link
    #         link=next
    #     link.next=pre
    #     return link
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #使用递归的方式
        #递归条件和处理条件
        # if link.next != None : 继续往下迭代
        # if link.next == None :  link.next=link.pre,并且返回Link头
        if head !=None and head.next !=None:
            return self.getReverseLink(head,head.next)
        return head

    def getReverseLink(self,preLink: Optional[ListNode],link: Optional[ListNode])-> Optional[ListNode]:

        if link.next != None :
            head=self.getReverseLink(link, link.next)
            link.next=preLink
            preLink.next = None
            return head
        else:
            link.next=preLink
            preLink.next=None
            return link