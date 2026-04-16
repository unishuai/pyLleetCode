# ============================================
# @File    : day38_230.py
# @Date    : 2026-04-16 8:53
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #这个直接用中序遍历出栈，然后是第K个
        p=root
        stack=[]
        count=0
        while p !=None or len(stack)>0:
            while p!=None:
                stack.append(p)
                p=p.left
            p=stack.pop()
            if p !=None:
                count+=1
                if count == k:
                    return p.val
            p=p.right
        return None


