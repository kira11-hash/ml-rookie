"""
题号：27. 移除元素（Remove Element）

题目描述（中文）：
给你一个数组 nums 和一个值 val。
你需要原地移除所有数值等于 val 的元素，并返回移除后数组的新长度。

要求：
1) 不要使用额外数组空间（必须原地修改）
2) 元素顺序可以改变（本题允许）
3) 返回的新长度记为 k，最终只需保证 nums 的前 k 个元素是保留结果

示例：
1) nums = [3,2,2,3], val = 3 -> 返回 2，nums 前两位可为 [2,2]
2) nums = [0,1,2,2,3,0,4,2], val = 2 -> 返回 5，前五位可为 [0,1,4,0,3]
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        slow = 0
        for fast in range(len(nums)):
           if nums[fast]!= val:
               nums[slow],nums[fast] = nums[fast],nums[slow]
               slow = slow+1
        
        del nums[slow:]
        return slow



