# ============================================
# @File    : day43_236.py
# @Date    : 2026-04-17 8:49
# @Author  : 帅宇昕
# ============================================
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     r=root
    #     stack=[]
    #
    #     depth=1
    #
    #     stack.append((root,depth))
    #     reslist=[]
    #     while  stack:
    #         r,depth=stack.pop()
    #         reslist.append((r,depth))
    #         if r.left !=None:
    #             stack.append((r.left,depth+1))
    #         if r.right !=None:
    #             stack.append((r.right, depth + 1))
    #     findp = False
    #     findq = False
    #     mindepth=float("inf")
    #     minNode=None
    #     for i in range(len(reslist)-1,-1,-1):
    #         tmpp,depth=reslist[i]
    #         if   depth <=mindepth:
    #             mindepth=depth
    #             minNode=tmpp
    #         if tmpp is p:
    #             findp=True
    #         elif tmpp is q:
    #             findq=True
    #         if findp and findq:
    #             return minNode

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     def getlowestAncestor(root, p, q):
    #         if root==None:
    #             return None
    #         if root==p or root==q:
    #             return root
    #         left=getlowestAncestor(root.left, p, q)
    #         right=getlowestAncestor(root.right, p, q)
    #         if left and right:
    #             return root
    #         if left :
    #             return left
    #         else:
    #             return right
    #
    #
    #
    #     return getlowestAncestor(root, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            #这个就是存储所有的节点的关系，他这个需要用到未来数据的方式，得存储
            if root==None:
                return
            if root.left!=None:
                parent[root.left.val]=root
                dfs(root.left)
            if root.right!=None:
                parent[root.right.val]=root
                dfs(root.right)


        parent={}
        visited=set()
        #这个是获取节点关系
        dfs(root)
        while p !=None:
            visited.add(p)
            p = parent.get(p.val)
        while q !=None:
            if q in visited:
                return q
            q=parent.get(q.val)
        return None

