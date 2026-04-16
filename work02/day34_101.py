# ============================================
# @File    : day34_101.py
# @Date    : 2026-04-15 15:54
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional





class Solution:
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     def judgeSymmetric(lp, rp):
    #         if lp==None and rp==None:
    #             return True
    #         elif lp==None and rp!=None:
    #             return False
    #         elif lp!=None and rp==None:
    #             return False
    #         # 都存在
    #         if lp.val == rp.val:
    #             lres=judgeSymmetric(lp.left,rp.right)
    #             rres=judgeSymmetric(lp.right, rp.left)
    #             if lres and rres :
    #                 return True
    #
    #         return False
    #     # 我感觉这个用递归会好一点
    #     if root ==None:
    #         return True
    #
    #     return judgeSymmetric(root.left,root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        stack=[]
        stack.append(root.left)
        stack.append(root.right)
        while len(stack)>0:
            r=stack.pop()
            l=stack.pop()
            if r==None and l==None:
                continue
            elif r==None or l==None or r.val!=l.val:
                return False
            if r.val==l.val:
                stack.append(l.left)
                stack.append(r.right)
                stack.append(l.right)
                stack.append(r.left)
        return True





