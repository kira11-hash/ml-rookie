"""
题号：1. 两数之和（Two Sum）

题目描述（中文）：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，
并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，且同一个元素不能重复使用。
返回答案顺序不限。

示例：
1) nums = [2,7,11,15], target = 9 -> [0,1]
2) nums = [3,2,4], target = 6 -> [1,2]
3) nums = [3,3], target = 6 -> [0,1]
"""

from typing import List


class Solution:
    # 方法1：暴力法
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

    # 方法2：哈希表法（推荐）
    # 复杂度：时间 O(n)，空间 O(n)
    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in mp:
                return [mp[need], i]
            mp[x] = i

    # LeetCode 默认入口：当前使用哈希法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSum_hash(nums, target)
