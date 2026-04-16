# ============================================
# @File    : day39_199.py
# @Date    : 2026-04-16 9:25
# @Author  : 帅宇昕
# ============================================
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #二叉树的右视图，这个是每层选一个
        # p=root
        # dq=collections.deque()
        # dq.append(root)
        # res=[]
        # while len(dq)>0:
        #     lstack=len(dq)
        #     lastp=None
        #     for i in range(lstack):
        #         p=dq.popleft()
        #         if p !=None:
        #             lastp=p
        #             dq.append(p.left)
        #             dq.append(p.right)
        #
        #     if lastp!=None:
        #         res.append(lastp.val)
        # return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        p=root
        stack=[]
        count=0
        stack.append((root,count))
        res=[]
        while stack:
            p,tmpcount=stack.pop()
            if p !=None:

                stack.append((p.left,tmpcount+1))
                stack.append((p.right,tmpcount+1))
                if count+1==tmpcount:
                    res.append(p.val)
                    count+=1




        return res