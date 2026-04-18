# ============================================
# @File    : day42_437.py
# @Date    : 2026-04-16 21:04
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
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     def getPathNum(root:TreeNode, prefix:dict, lastSum:int,targetSum:int):
    #         if root==None:
    #             return 0
    #         currentSum=lastSum+root.val
    #         res=prefix.get(currentSum-targetSum,0)
    #         prefix[currentSum]=prefix.get(currentSum,0)+1
    #         res += getPathNum(root.left, prefix, currentSum, targetSum)
    #         res += getPathNum(root.right, prefix, currentSum, targetSum)
    #         #还原现场，因为这个不会复制一份
    #         prefix[currentSum] = prefix.get(currentSum, 0) -1
    #         return res
    #
    #     prefix={0:1}
    #     lastSum=0
    #     return getPathNum(root, prefix, lastSum, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def getSum(root, targetSum):
            if root == None:
                return 0
            needSum = targetSum - root.val
            res = 0
            if needSum == 0:
                res += 1
            res+=getSum(root.left, needSum)
            res+=getSum(root.right, needSum)
            return res

        if root==None:
            return 0
        # needSum=targetSum-root.val
        # res=0
        # if needSum==0:
        #     res+=1
        res=getSum(root,targetSum)
        res+=self.pathSum(root.left,targetSum)
        res+=self.pathSum(root.right, targetSum)
        return res
