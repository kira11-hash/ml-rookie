"""
题号：167. 两数之和 II - 输入有序数组（Two Sum II - Input Array Is Sorted）

题目描述（中文）：
给你一个下标从 1 开始的整数数组 numbers，该数组已按非递减顺序排列。
请你从数组中找出满足下列条件的两个数：
1) 两数之和等于目标值 target
2) 不能使用同一个元素两次

返回这两个数的下标 [index1, index2]（下标从 1 开始）。
题目保证恰好存在一个解。

示例：
1) numbers = [2,7,11,15], target = 9 -> [1,2]
2) numbers = [2,3,4], target = 6 -> [1,3]
3) numbers = [-1,0], target = -1 -> [1,2]
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # TODO 1: 初始化双指针 l=0, r=len(numbers)-1

        # TODO 2: while l < r:
        #   - 计算 s = numbers[l] + numbers[r]
        #   - 如果 s == target: 返回 [l+1, r+1]（注意题目是 1-based）
        #   - 如果 s < target: l += 1
        #   - 如果 s > target: r -= 1
        l=0
        r=len(numbers)-1
        while l<r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                 l += 1
            else:
                 r -= 1
        # TODO 3: 理论上题目保证有解，这里仅做兜底
        return []