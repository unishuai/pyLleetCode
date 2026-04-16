# ============================================
# @File    : day37_98.py
# @Date    : 2026-04-15 22:09
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
from typing import Optional
from winreg import QueryInfoKey


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     # 左边最大值 < 根  < 右边最大值
    #     if root==None:
    #         return True
    #
    #     #判断是不是BST，主要就是判断中序遍历是不是递增的
    #     queue=[]
    #
    #     res=[]
    #     p=root
    #     while p!=None  or len(queue)>0:
    #         while p!=None:
    #             queue.append(p)
    #             p=p.left
    #
    #         p=queue.pop()
    #         if p !=None:
    #             res.append(p.val)
    #         p=p.right
    #
    #     tmp=res[0]
    #     for i in range(1,len(res)):
    #         if tmp>=res[i]:
    #             return False
    #         tmp=res[i]
    #     return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def judgeBST(root, nmin, nmax):
            if root==None:
                return True
            if root.val<=nmin or root.val>=nmax:
                return False
            judgeLeft=judgeBST(root.left, nmin, root.val)
            judgeRight=judgeBST(root.right, root.val, nmax)
            if judgeLeft and judgeRight:
                return True
            return False


        if root ==None:
            return True

        return judgeBST(root,float("-inf"),float("inf"))






