# ============================================
# @File    : day40_114.py
# @Date    : 2026-04-16 10:52
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
from sys import flags
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     p=root
    #     pre=TreeNode()
    #     pre.right=root
    #     stack=[p]
    #     while stack:
    #         p=stack.pop()
    #         if p !=None:
    #             stack.append(p.right)
    #             stack.append(p.left)
    #             pre.right=p
    #             pre.left=None
    #             pre=p
    #
    #     return pre.right

    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr



