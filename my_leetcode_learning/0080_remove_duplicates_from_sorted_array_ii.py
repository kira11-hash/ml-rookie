"""
LeetCode 80. 删除有序数组中的重复项 II

题目描述（中文）：
给你一个有序数组 nums，请你原地删除重复出现的元素，使得每个元素最多只出现两次，
返回删除后数组的新长度。

不要使用额外数组空间，你必须在原地修改输入数组并在 O(1) 额外空间条件下完成。

说明：
- 返回值 k 表示去重后有效长度
- nums 的前 k 个元素应为处理后的结果
- nums 后面的内容不重要（LeetCode 判题只检查前 k 个）

示例：
输入：nums = [1,1,1,2,2,3]
输出：5，前 5 个元素为 [1,1,2,2,3]
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # 长度<=2，不可能违规，直接返回

        slow = 2  # 前两个直接保留，slow指向下一个待写入位置

        for fast in range(2, len(nums)):
            # 问：nums[fast] 放入有效区间，会不会变成第3个重复？
            # 只需和有效区间倒数第2个比（即 nums[slow - 2]）
            if nums[fast] != nums[slow - 2]:
                # 不等 -> 没超限 -> 写入有效区间
                nums[slow] = nums[fast]
                slow += 1
            # 相等 -> 已经有2个了 -> 跳过，什么都不做

        return slow  # slow 就是有效区间的长度


if __name__ == "__main__":
    # 本地简单自测（可取消注释）
    # s = Solution()
    # arr = [1, 1, 1, 2, 2, 3]
    # k = s.removeDuplicates(arr)
    # print(k, arr[:k])  # 期望: 5 [1,1,2,2,3]
    pass
