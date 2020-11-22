## 第八周学习笔记

### 十大经典排序算法python实现
#### 1.选择排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort 
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                    #print(nums)
        return nums
```
#### 2.冒泡排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort 
        n = len(nums)
        # 进行多次循环
        for c in range(n):
            for i in range(1, n - c):
                if nums[i - 1] > nums[i]:
                 nums[i - 1], nums[i] = nums[i], nums[i - 1]
        return nums
```
#### 3.插入排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insert sort 
        n = len(nums)
        for i in range(1,n):
            while i > 0 and nums[i-1] > nums[i]:
                nums[i-1],nums[i] = nums[i],nums[i-1]
                i -= 1
        return nums
```
#### 4.希尔排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #shell sort
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i - gap >= 0 and nums[i - gap] > nums[i]:
                    nums[i - gap], nums[i] = nums[i], nums[i - gap]
                    i -= gap
            gap //= 2
        return nums
```
#### 5.归并排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort
        res = []
        mid = len(nums) //2
        left, right = nums[:mid],nums[mid:]
        if len(left) > 1: left = self.sortArray(left)
        if len(right) > 1: right = self.sortArray(right)

        while left and right:
            if left[-1] >= right[-1]:
                res.append(left.pop())
            else:
                res.append(right.pop())
        res.reverse()
        return (left or right) + res  # 将剩余left或right中的数和res合并
```
#### 6.快速排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #quick sort
        n = len(nums)
        first = 0
        last = n - 1
        self.quickSorthepler(nums,first,last)
        return nums

    def partition(self, alist, first, last):
        left = first
        right = last
        pivot = alist[first]
        while left < right:
            while left < right and alist[right] >= pivot:
                right -= 1
            alist[left] = alist[right]
            while left < right and alist[left] <= pivot:
                left += 1
            alist[right] = alist[left]
        alist[left] = pivot
        return left
    
    def quickSorthepler(self, alist, first,last):
        if first < last:
            pointmark = self.partition(alist,first,last)
            self.quickSorthepler(alist,first,pointmark-1)
            self.quickSorthepler(alist, pointmark + 1, last)
```
#### 7.堆排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #heap sort
        n = len(nums)
        def build_heap(nums, start, end):  # 建堆的同时调整堆
            newitem = nums[start]
            cur = start
            leftpos = 2 * cur + 1
            while leftpos < end:
                rightpos = leftpos + 1
                if rightpos < end and nums[rightpos] >= nums[leftpos]:
                    leftpos = rightpos
                if newitem < nums[leftpos]:
                    nums[cur] = nums[leftpos]
                    cur = leftpos
                    leftpos = 2 * cur + 1
                else:
                    break
            nums[cur] = newitem
        for i in reversed(range(n//2)):  # 建堆+调整
            build_heap(nums, i, n)
        for i in range(n-1,-1,-1):
            nums[0],nums[i] = nums[i],nums[0]  #排序
            build_heap(nums,0,i)  #调整
        return nums
```
#### 8.计数排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        from collections import defaultdict

        def counter_sort(nums,key=lambda x:x):
            #counter sort
            B,C = [], defaultdict(list)
            for x in nums:
                C[key(x)].append(x)  #  {1:1,2:2,......}
            for k in range(min(C), max(C) + 1):
                B.extend(C[k])
            return B
        res = counter_sort(nums)
        return res
```
#### 9.桶排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #bucket sort
        if len(nums) < 2:
            return nums
        _min = min(nums)
        _max = max(nums)
        # 需要桶个数
        bucketNum = (_max - _min) // bucketSize + 1
        buckets = [[] for _ in range(bucketNum)]
        for num in nums:
            # 放入相应的桶中
            buckets[(num - _min) // bucketSize].append(num)
        res = []

        for bucket in buckets:
            if not bucket: continue
            if bucketSize == 1:
                res.extend(bucket)
            else:
                # 当都装在一个桶里,说明桶容量大了
                if bucketNum == 1:
                    bucketSize -= 1
                res.extend(bucket_sort(bucket, bucketSize))
        return res
```
#### 10.基数排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #radix sort
        if not nums: return []
        _max = max(nums)
        # 最大位数
        maxDigit = len(str(_max))
        bucketList = [[] for _ in range(10)]
        # 从低位开始排序
        div, mod = 1, 10
        for i in range(maxDigit):
            for num in nums:
                bucketList[num % mod // div].append(num)
            div *= 10
            mod *= 10
            idx = 0
            for j in range(10):
                for item in bucketList[j]:
                    nums[idx] = item
                    idx += 1
                bucketList[j] = []
        return nums
```