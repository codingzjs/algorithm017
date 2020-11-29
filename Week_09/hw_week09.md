
#### 541. 反转字符串 II
[leetcode#541-reverse-string-ii](https://leetcode-cn.com/problems/reverse-string-ii/)

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slist = list(s)
        for i in range(0, len(slist), 2 * k):
            slist[i:i+k] = reversed(slist[i:i+k])
        return "".join(slist)
```
#### 91. 解码方法
[leetcode#91-decode-ways](https://leetcode-cn.com/problems/decode-ways/)

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        size=len(s)
        if not s or s[0]=="0":
            return 0
        dp=[0]*(size+1)
        dp[0], dp[1] = 1, 1
        #dp[i]表示s[:i-1]的解码方法
        for i in range(1,size):
            if s[i]=="0":#如果当前位为0
                if s[i-1] == "1" or s[i-1] == "2":#它最多能与前一位合并，也就是与s[:i-2]的解码方法树相同-->dp[i-1]
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
            #s[i]!='0'说明有可能可以单独解码，也可能与上一个合并后解码
            # s[i]单独解码--> 解码总数与s[:i-1]的解码方法一致 --> dp[i]
            # s[i]与s[i-1]合并解码 -->解码总数与s[:i-2]的解码方法总数一致-->dp[i-1]
                if '10'<=s[i-1:i+1]<='26':
                    dp[i+1] = dp[i]+dp[i-1] 
                else:
                    dp[i+1] = dp[i]
        return dp[-1]
```
