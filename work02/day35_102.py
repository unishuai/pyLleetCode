# ============================================
# @File    : day35_102.py
# @Date    : 2026-04-15 20:15
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     queue=collections.deque()
    #     res=[]
    #     count=1
    #     queue.append((root,count))
    #     tmpres=[]
    #     while len(queue)>0:
    #         tmp,depth=queue.popleft()
    #         if tmp!=None:
    #
    #             if depth==count+1:
    #                 count+=1
    #                 res.append(tmpres)
    #                 tmpres = []
    #             tmpres.append(tmp.val)
    #             queue.append((tmp.left, count + 1))
    #             queue.append((tmp.right, count + 1))
    #     if len(tmpres)>0:
    #         res.append(tmpres)
    #     return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=collections.deque()
        res=[]
        count=1
        queue.append(root)


        while len(queue)>0:
            qlen=len(queue)
            tmpres = []
            for i in range(qlen):
                p=queue.popleft()
                if p !=None:
                    tmpres.append(p.val)
                    queue.append(p.left)
                    queue.append(p.right)
            if len(tmpres)>0:
                res.append(tmpres)
        return res








    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if root ==None:
    #         return list()

