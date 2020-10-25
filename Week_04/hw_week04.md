
#### 860. 柠檬水找零
[leetcode#860-lemonade-change](https://leetcode-cn.com/problems/lemonade-change/)


```python
#此题思路主要是找零的所有情况理清，找零时10+5优先于3*5
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
```
#### 122. 买卖股票的最佳时机 II
[leetcode#122-best-time-to-buy-and-sell-stock-ii](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

```python
#主要思路为等价于每天都做买卖：遍历整个股票交易日价格列表price
#所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0: profit += tmp
        return profit
```
#### 455. 分发饼干
[leetcode#455-assign-cookies](https://leetcode-cn.com/problems/assign-cookies/description/)

```python
#先排序。利用贪心算法的思想：每次都先满足胃口最小的孩子，直到有效饼干分完，
#或者小胃口孩子都被满足则停止分发。
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = 0
        for size in s:
            if n == len(g):
                break
            if size >= g[n]:
                n += 1
        return n
```