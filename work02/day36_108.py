# ============================================
# @File    : day36_108.py
# @Date    : 2026-04-15 21:42
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getBST(nums, l, r):
            if l == r:
                return TreeNode(nums[l])
            elif l > r:
                return None
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            root.left=getBST(nums, l, mid-1)
            root.right=getBST(nums, mid+1, r)
            return root



        return getBST(nums,0,len(nums)-1)
