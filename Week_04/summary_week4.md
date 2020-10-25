## 第四周学习笔记

### 贪心算法和动态规划：
**相同点**：都是一种递推算法 即均由局部最优解来推导全局最优解

**不同点**：

**贪心算法**： 每一步的最优解一定包含上一步的最优解，上一步之前的最优解则不作保留，换句话说就是一开始就定好了最优策略

**动态规划**：记录之前的所有的局部最优解，可以列出递归公式。代码非常套路，一般都是设一个二维数组或者一维数组记录中间结果。

### 贪心算法题目：

[122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

[455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/)

[860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)

[874. 模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/)

[944. 删列造序](https://leetcode-cn.com/problems/delete-columns-to-make-sorted/)

[1005. K 次取反后最大化的数组和](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/)

