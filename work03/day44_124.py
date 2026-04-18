# ============================================
# @File    : day44_12.py
# @Date    : 2026-04-17 16:32
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

    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     maxNum = float('-inf')
    #     maxlist=[maxNum]
    #     def getMaxNum(root, parentNum):
    #         if root == None:
    #             return 0
    #         # 这个是知道父节点开始计算
    #         if parentNum < 0:
    #             currentNum = root.val
    #         else:
    #             currentNum = parentNum + root.val
    #         maxlist[0]=max(maxlist[0], currentNum)
    #         leftNum = getMaxNum(root.left, currentNum)
    #
    #         if leftNum <0:
    #             currentNum2=root.val
    #         else:
    #             currentNum2 = leftNum+root.val
    #         maxlist[0] = max(maxlist[0], currentNum2 + currentNum-root.val)
    #         currentNum2=max(currentNum2,currentNum)
    #         maxlist[0]=max(maxlist[0], currentNum2)
    #
    #
    #         getMaxNum(root.right, currentNum2)
    #         return max(leftNum+root.val,root.val)
    #
    #     parentNum=0
    #     getMaxNum(root,parentNum)
    #     return maxlist[0]




    def __init__(self):
        self.maxNum=float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getMax(root):
            if root==None:
                return 0
            left=max(getMax(root.left),0)
            right=max(getMax(root.right), 0)
            self.maxNum=max(self.maxNum,left+root.val+right)
            return max(left+root.val,right+root.val)


        if root==None:
            return 0
        getMax(root)
        return self.maxNum

