# ============================================
# @File    : day29_148.py
# @Date    : 2026-04-13 21:40
# @Author  : 帅宇昕
# ============================================
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





class Solution:
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #
    #     if head==None or head.next==None:
    #         return head
    #     prehead=ListNode()
    #     prehead.next=head
    #     p=prehead
    #     slow=head
    #     fast=head
    #     while fast.next !=None and fast.next.next!=None:
    #         slow=slow.next
    #         fast=fast.next.next
    #     # if fast.next!=None:
    #     #     fast=fast.next
    #
    #     mid = slow.next
    #     slow.next=None
    #     leftp=self.sortList(head)
    #     rightp =self.sortList(mid)
    #     while leftp!=None and rightp!=None:
    #         if leftp.val<rightp.val:
    #             p.next=leftp
    #             p=leftp
    #             leftp=leftp.next
    #         else:
    #             p.next = rightp
    #             p = rightp
    #             rightp = rightp.next
    #
    #     if leftp==None:
    #         p.next=rightp
    #     else:
    #         p.next = leftp
    #     return prehead.next

    def sortList(self, head: ListNode) -> ListNode:
        h,lengh,intv = head , 0, 1
        #要想做二分，必须先知道这个的长度
        while h:
            h=h.next
            lengh=lengh+1
        res=ListNode()
        res.next=head
        #现在获取了长度，然后还是循环
        while intv <lengh:
            pre=res
            p=res.next
            while p :
                p1=p
                i = intv
                while i and p:
                    i-=1
                    p=p.next
                if i>0: #没有h2，不需要合并
                    break
                p2=p
                i=intv
                while i and p :
                    p=p.next
                    i=i-1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                #合并
                while c1 and c2:
                    if p1.val<p2.val:
                        pre.next=p1
                        p1=p1.next
                        c1-=1
                    else:

                        pre.next = p2
                        p2 = p2.next
                        c2-=1
                    pre=pre.next
                pre.next = p1 if c1 else p2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = p
            intv *= 2
        return res.next









