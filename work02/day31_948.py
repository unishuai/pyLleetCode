# ============================================
# @File    : day31_23.py
# @Date    : 2026-04-14 11:01
# @Author  : 帅宇昕
# ============================================
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left: Optional["TreeNode"]=None , right: Optional["TreeNode"]=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root==None:
    #         return list()

    #     leftList=self.inorderTraversal(root.left)
    #     rootVal=root.val
    #     rightList=self.inorderTraversal(root.right)
    #     # if len(leftList)<1 and len(rightList)<1:
    #     #     return [rootVal]
    #     # elif len(leftList)<1:
    #     #     return leftList.append(rootVal)
    #     # elif len(rightList)<1:
    #     #     return [rootVal].extend(rightList)
    #     # else:
    #     #     return leftList.append(rootVal).extend(rightList)
    #     return leftList+[rootVal]+rightList

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None :
            return []
        stack=[]

        res=[]
        p=root

        while p !=None or len(stack)>=1:
            while p!=None:
                stack.append(p)
                p=p.left
            p=stack.pop()
            res.append(p.val)
            p=p.right
        return res






