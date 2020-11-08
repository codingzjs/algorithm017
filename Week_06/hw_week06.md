
#### 64. 最小路径和
[leetcode#64-minimum-path-sum](https://leetcode-cn.com/problems/minimum-path-sum/)

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for row in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[rows - 1][columns - 1]
```
#### 91. 解码方法
[leetcode#91-decode-ways](https://leetcode-cn.com/problems/decode-ways/)

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0 
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[i+1] += dp[i]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[i+1] += dp[i-1]
        
        return dp[-1]
```
