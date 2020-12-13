## 第九周学习笔记

#### 63. 不同路径 II
[leetcode#63-unique-paths-ii](https://leetcode-cn.com/problems/unique-paths-ii/)
```python
#状态转移方程：dp[i][j]=dp[i−1,j]+dp[i,j−1] if(i,j)上无障碍物
# dp[i][j]= 0 if(i,j)上有障碍物
# dp[i][j] 表示走到格子(i,j)的方法数
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        r, l = len(obstacleGrid), len(obstacleGrid[0])

        for i in range(r):

            for j in range(l):

                if obstacleGrid[i][j] != 1:

                    if i == 0 and j == 0:

                        obstacleGrid[i][j] = 1

                    elif i == 0 and j != 0:

                        obstacleGrid[i][j] = obstacleGrid[i][j-1]

                    elif i != 0 and j == 0:

                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]

                    else:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[r - 1][l - 1]
```