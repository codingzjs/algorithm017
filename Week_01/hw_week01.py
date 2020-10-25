#-*- encoding:utf-8 -*-

#作业

#26.删除排序数组中对重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(sorted(set(nums)))
        return len(nums)

#1.两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, nums_one in enumerate(nums):
            nums_two = target - nums_one
            if nums_two in dic:
                return [dic[nums_two], index]
            dic[nums_one] = index
        return None

#283.移动零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

#66.加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = 0
        for i in range(len(digits)):
            nums += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(j) for j in str(nums + 1)]

#189.旋转数组
#21.合并两个有序链表
#88.合并两个有序数组
#641.设计循环双端队列
#42.接雨水
