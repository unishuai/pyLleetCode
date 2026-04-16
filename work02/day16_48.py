# ============================================
# @File    : day16_48.py
# @Date    : 2026-04-09 15:34
# @Author  : 帅宇昕
# ============================================
from typing import List


class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     #"这个是矩阵，行列相等"
    #     mlen=len(matrix)
    #     if mlen<=1:
    #         return
    #     maxStep=mlen//2
    #     for i in range(maxStep):
    #
    #         for j in range(i,mlen-i-1):
    #             m0=i
    #             n0=j
    #
    #             #第一个替换第二个
    #             m1 = n0
    #             n1 = mlen - m0-1
    #             tmp=matrix[m1][n1]
    #             matrix[m1][n1]=matrix[m0][n0]
    #
    #             #第二个替换第三个
    #             m2 = n1
    #             n2 = mlen - m1 - 1
    #             nextTmp = matrix[m2][n2]
    #             matrix[m2][n2] = tmp
    #             tmp=nextTmp
    #
    #             # 第三个替换第四个
    #             m3 = n2
    #             n3= mlen - m2 - 1
    #             nextTmp = matrix[m3][n3]
    #             matrix[m3][n3] = tmp
    #             tmp = nextTmp
    #
    #             # 第四个替换第一个
    #             matrix[i][j]=tmp


        # print(matrix)


    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n//2):
            for j in range(n+1//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp

                # #第一个位置
                # matrix[i][j]
                # #第二个位置
                # matrix[n-j-1][i]
                # #滴三个位置
                # matrix[n-i-1][n-j-1]
                # #第四个位置
                # matrix[j][n-i-1]




# t=Solution()
# t.rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])