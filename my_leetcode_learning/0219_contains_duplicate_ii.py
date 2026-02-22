"""
题号：219. 存在重复元素 II（Contains Duplicate II）

题目描述（中文）：
给你一个整数数组 nums 和一个整数 k。
判断数组中是否存在两个不同下标 i 和 j，使得：
1) nums[i] == nums[j]
2) abs(i - j) <= k

如果存在，返回 True；否则返回 False。

示例：
1) nums = [1,2,3,1], k = 3 -> True
2) nums = [1,0,1,1], k = 1 -> True
3) nums = [1,2,3,1,2,3], k = 2 -> False
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i,x in enumerate(nums):
            if x in mp:
                if i-mp[x]<=k:
                    return True
            mp[x]=i
        return False

            
            
        
    
            

