# ============================================
# @File    : day46_994.py
# @Date    : 2026-04-18 17:02
# @Author  : 帅宇昕
# ============================================
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 这个题目使用深度优先和广度优先区别不大
        # 重点是需要找到扩散的起点
        row=len(grid)
        line=len(grid[0])
        orange=0
        queue=collections.deque()
        times=0
        for i in range(row):
            for j in range(line):
                if grid[i][j]==2:
                    queue.append((i,j,times))
                elif grid[i][j]==1:
                    orange+=1
        if orange == 0:
            return times
        #然后开始广度优先，
        while len(queue)>0:
            x,y,times=queue.popleft()
            #上
            if x-1>=0 and grid[x-1][y]==1:
                grid[x - 1][y]=2
                queue.append((x-1,y,times+1))
                orange-=1
            if y-1>=0 and grid[x][y-1]==1:
                grid[x][y-1]=2
                queue.append((x , y-1,times+1))
                orange -= 1
            if x+1<row and grid[x+1][y]==1:
                grid[x+1][y]=2
                queue.append((x+1,y,times+1))
                orange-=1
            if y+1<line and grid[x][y+1]==1:
                grid[x][y+1]=2
                queue.append((x,y+1,times+1))
                orange-=1
            if orange==0:
                return times+1
        return -1





