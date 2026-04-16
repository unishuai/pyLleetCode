# ============================================
# @File    : day33_226.py
# @Date    : 2026-04-15 11:34
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
from functools import total_ordering


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     #感觉可以用广度优先
    #     stack=[]
    #     head=root
    #     p=root
    #     stack.append(root)
    #     while  len(stack)>0:
    #         p=stack.pop()
    #         if p !=None:
    #             stack.append(p.left)
    #             stack.append(p.right)
    #             #交换左右子树
    #             tmp=p.left
    #             p.left=p.right
    #             p.right=tmp
    #     return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     #感觉可以用广度优先
    #     stack=[]
    #     head=root
    #     p=root
    #     stack.append(root)
    #     while  len(stack)>0:
    #         p=stack.pop()
    #         if p !=None:
    #             stack.append(p.left)
    #             stack.append(p.right)
    #             #交换左右子树
    #             tmp=p.left
    #             p.left=p.right
    #             p.right=tmp
    #     return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     #感觉可以用广度优先
    #     stack=[]
    #     head=root
    #     p=root
    #     stack.append(root)
    #     while  len(stack)>0:
    #         p=stack.pop()
    #         if p !=None:
    #             stack.append(p.left)
    #             stack.append(p.right)
    #             #交换左右子树
    #             tmp=p.left
    #             p.left=p.right
    #             p.right=tmp
    #     return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None :
            return root
        #
        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp=root.left
        root.left=root.right
        root.right=tmp



        return root




