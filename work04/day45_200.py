# ============================================
# @File    : day45_200.py
# @Date    : 2026-04-18 15:33
# @Author  : 帅宇昕
# ============================================
from typing import List





class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsSetLand(landlist, i, j, num):
            rlen=len(landlist)
            llen=len(landlist[0])
            if i<0 or i>=rlen or j<0 or j>=llen or landlist[i][j]==0 or landlist[i][j]==num:
                return
            landlist[i][j] = num
            dfsSetLand(landlist, i - 1, j, num)
            dfsSetLand(landlist, i + 1, j, num)
            dfsSetLand(landlist, i , j-1, num)
            dfsSetLand(landlist, i , j+1, num)

        #判断这个是不是一个陆地，第二个是判断这是不是一个新陆地
        #是海洋的话直接下一个就好
        #不是海洋，判断是不是一个新岛屿，我们可以通过每次遍历一行，然后上面和左边这已遍历的地方，是不是存在岛屿，
            # 存在就判断他们是不是一致的，一致的直接过，如果不是一直的，就要更新岛屿，更新用深度优先更新
        row=len(grid)
        line=len(grid[0])
        landlist=[[0]*line for i in range(row)]
        landNum=1
        countLand=0
        land='1'
        ocean='0'
        for i in range(row):
            for j in range(line):
                if grid[i][j]==land:
                    upNum = ocean
                    leftNum=ocean
                    if i-1>=0:
                        upNum=grid[i - 1][j]
                    if j-1>=0:
                        leftNum=grid[i ][j-1]

                    if upNum==ocean and leftNum==ocean:
                        landlist[i][j]=landNum
                        landNum+=1
                        countLand+=1
                    elif upNum ==land and leftNum==land:
                        landlist[i][j] = landlist[i ][j-1]
                        #等于1必须就是大陆，不在边缘
                        if landlist[i - 1][j] != landlist[i][j-1]:


                            # landlist[i-1][j] = landlist[i][j - 1]
                            num=landlist[i][j-1]
                            dfsSetLand(landlist,i-1,j,num)
                            countLand-=1

                    elif upNum ==land:

                        landlist[i][j] = landlist[i-1 ][j]
                    else:
                        landlist[i][j] = landlist[i ][j-1]

        return  countLand

