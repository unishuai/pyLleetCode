# Definition for a binary tree node.
from typing import Optional, Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # 最大深度可以用递归或者刚刚的那个堆栈去算
    #     # def getDepth(root):
    #     if root == None:
    #         return 0
    #     depth = 1
    #     left = self.maxDepth(root.left)
    #     right = self.maxDepth(root.right)
    #     return depth + max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 最大深度可以用递归或者刚刚的那个堆栈去算
        if root ==None:
            return 0

        stack=[]
        maxNum = 1
        current=0
        p=root
        while p!=None or len(stack)>0:
            while p!=None:
                current += 1
                stack.append((p,current))
                p=p.left

            p,current=stack.pop()
            if current >maxNum:
                maxNum=current

            p=p.right


        return maxNum





