# ============================================
# @File    : day55_131.py
# @Date    : 2026-04-20 15:55
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def partition(self, s: str) -> List[List[str]]:
    #     res=[]
    #     tmplist=[]
    #     def judgePart(palindrome,i,j) ->bool:
    #         while i<j:
    #             if palindrome[i]!=palindrome[j]:
    #                 return False
    #             i+=1
    #             j-=1
    #         return True
    #
    #
    #     def dfs(s, depth):
    #         if depth==len(s):
    #             res.append(tmplist[:])
    #         for i in range(depth,len(s)):
    #             if judgePart(s,depth,i):
    #                 tmplist.append(s[depth:i+1])
    #                 dfs(s,i+1)
    #                 tmplist.pop()
    #
    #     depth=0
    #     #这个说白了，也只有确定是什么分类了，才好确定是不是回文
    #     #这个是每一个数都得参加
    #     dfs(s,depth)
    #     return res

    def partition(self, s: str) -> List[List[str]]:
        res=[]
        tmplist=[]



        def dfs(s, depth):
            if depth==len(s):
                res.append(tmplist[:])
            for i in range(depth,len(s)):
                if parlindromedp[depth][i]:
                    tmplist.append(s[depth:i+1])
                    dfs(s,i+1)
                    tmplist.pop()



        # 因为递归的时候，每次都需要判断这个回文子串，做了很多重复的工作，这里我们可以节约时间
        # 把每一个回文子串是否满足要求都存储起来
        slen=len(s)
        parlindromedp=[[True]*(slen+1) for i in range(slen+1)]
        #这里要看递归的时候是+1还是-1，然后才能确定数组的循环损失
        for i in range(slen-1,-1,-1):
            for j in range(i+1,slen):
                #(i,j) f(i+1,j+1)=f(i,j) and s[i]==s[j]

                parlindromedp[i][j]=parlindromedp[i+1][j-1] and s[i]==s[j]


        depth=0
        #这个说白了，也只有确定是什么分类了，才好确定是不是回文
        #这个是每一个数都得参加
        dfs(s,depth)
        return res