# ============================================
# @File    : day47_207.py
# @Date    : 2026-04-18 19:26
# @Author  : 帅宇昕
# ============================================
import collections
from typing import List


class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     #这个题目的主要目的，就是判断有没有环
    #     mp={}
    #     for requisites in prerequisites:
    #         if requisites[0] in mp:
    #             mp[requisites[0]]=mp[requisites[0]].append(requisites[1])
    #         else:
    #             mp[requisites[0]]=[requisites[1]]
    #
    #     visited=[0]*numCourses
    #     stack=[]
    #     for i in range(numCourses):
    #         if visited[i]==0 and i in mp:
    #             visited[i]=1
    #             stack.append(i)
    #             while stack:
    #                 p =stack.pop()
    #                 if j not in mp[p]:
    #                     reqCourse=mp[p]
    #                 for j in range(len(reqCourse)):
    #                     stack.append(reqCourse[j])



    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     #使用广度优先的方式解决这个问题
    #     #构造节点和边
    #     mp=collections.defaultdict(list)
    #     edges=[0]*numCourses
    #     for requisites in prerequisites:
    #         mp[requisites[1]].append(requisites[0])
    #         edges[requisites[0]]+=1
    #     dq=collections.deque()
    #     count=0
    #     for i in range(len(edges)):
    #         if edges[i]==0:
    #             dq.append(i)
    #             count+=1
    #             if count==numCourses:
    #                 return True
    #     while dq:
    #         p=dq.pop()
    #         outedges=mp[p]
    #         for outedge in outedges:
    #             edges[outedge]-=1
    #             if edges[outedge]==0:
    #                 dq.append(outedge)
    #                 count+=1
    #                 if count == numCourses:
    #                     return True
    #     return count == numCourses
    def __init__(self):
        self.valid=True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.valid=True
        def dfs(node):
            visited[node]=1
            tmp=mp[node]
            for i in  tmp:
                if visited[i]==0:
                    dfs(i)
                    if self.valid is False:
                        return
                elif visited[i]==1:
                    self.valid=False
                    return
            visited[node]=2


        mp=collections.defaultdict(list)
        for requisites in prerequisites:
            mp[requisites[1]].append(requisites[0])
        visited=[0]*numCourses
        for i in range(numCourses):
            if visited[i]==0:
                dfs(i)
        return self.valid







