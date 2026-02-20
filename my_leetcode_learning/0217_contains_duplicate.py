"""
题号：217. 存在重复元素（Contains Duplicate）

题目描述（中文）：
给你一个整数数组 nums。
如果任意一个值在数组中出现至少两次，返回 True；
如果数组中每个元素互不相同，返回 False。

示例：
1) nums = [1,2,3,1] -> True
2) nums = [1,2,3,4] -> False
3) nums = [1,1,1,3,3,4,3,2,4,2] -> True
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TODO 1: 创建一个空集合 seen
        seen=set()
        # TODO 2: 遍历 nums 中每个元素 x
        #   - 如果 x 已经在 seen 中，直接返回 True
        #   - 否则把 x 加入 seen
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        # TODO 3: 遍历结束仍没发现重复，返回 False
        return False
