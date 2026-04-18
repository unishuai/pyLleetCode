# ============================================
# @File    : day41_105.py
# @Date    : 2026-04-16 15:05
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
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if len(preorder)==0:
    #         return None
    #     elif len(preorder)==1:
    #         return TreeNode(preorder[0])
    #     root=TreeNode(preorder[0])
    #     rindex=None
    #     for i in range(len(inorder)):
    #         if inorder[i]==preorder[0]:
    #             rindex=i
    #             break
    #     root.left=self.buildTree(preorder[1:rindex+1],inorder[0:rindex])
    #     root.right=self.buildTree(preorder[rindex + 1:], inorder[rindex+1:])
    #     return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        elif len(preorder)==1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        stack=[]
        stack.append(root)

        # while stack:
        #     p=stack.pop()
        #     while inorder[inorderIndex]!=p.val:
        #
        #         q=TreeNode(preorder[preorderIndex])
        #         p.left=q
        #         p=q
        #         preorderIndex+=1
        #         stack.append(p)
        #     if inorder[inorderIndex]==p.val:
        #         while inorder[inorderIndex]==p.val:
        #             p=stack.pop()
        #             inorderIndex+=1
        #         p.right=  TreeNode(preorderVal)
        inorderIndex=0
        for i in range(1,len(preorder)):
            preorder_val=preorder[i]
            #这个p是用来判断是不是到分界线了
            p=stack[-1]
            if p.val !=inorder[inorderIndex]:
                p.left=TreeNode(preorder_val)
                stack.append(p.left)
            else:
                while stack and stack[-1].val==inorder[inorderIndex]:
                    p=stack.pop()
                    inorderIndex+=1
                p.right=TreeNode(preorder_val)
                stack.append(p.right)
        return root










