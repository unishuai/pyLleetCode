# ============================================
# @File    : day30_23.py
# @Date    : 2026-04-14 10:50
# @Author  : 帅宇昕
# ============================================
# 先放着asdas
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def getList(lists, l, r)-> Optional[ListNode]:
            if l+1==r:
                return lists[l]
            if l>=r:
                return None
            #这就是l<R了，然后f(l,r)=合并（f(l,mid)，f(mid+1,right)）
            mid=(l+r)//2
            lp=getList(lists, l, mid)
            rp = getList(lists, mid,r)
            pre=ListNode()
            res=pre
            while lp!=None and rp !=None:
                if lp.val<rp.val:
                    pre.next=lp
                    pre=lp
                    lp=lp.next
                else:
                    pre.next = rp
                    pre = rp
                    rp = rp.next
            if lp==None:
                pre.next=rp
            else:
                pre.next = lp
            return res.next


        #这个可以按照顺序合并，或者使用二分法，更快的合并
        return getList(lists,0,len(lists))