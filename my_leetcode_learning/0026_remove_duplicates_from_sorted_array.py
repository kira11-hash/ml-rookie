"""
LeetCode 26. 删除有序数组中的重复项

题目描述（中文）：
给你一个按 非递减顺序 排列的整数数组 nums，请你 原地 删除重复出现的元素，
使每个元素只出现一次，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

说明：
- 结果应使 nums 的前 k 个元素为唯一元素（顺序保持不变）
- 返回 k（唯一元素个数）
- nums 后面的内容不重要（LeetCode 判题只检查前 k 个）

示例：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 边界：空数组没有元素，去重后长度就是 0
        if not nums:
            return 0

        # slow 统一定义成“下一个写入位置”（也可理解为当前有效长度）
        # 初始时第 1 个元素一定保留，所以有效长度 = 1，下一次写入位置就是下标 1
        slow = 1
        # fast 从下标 1 开始扫描；因为数组有序，只需与“有效区间最后一个值”比较
        for fast in range(1, len(nums)):
            # 有效区间最后一个值在 nums[slow - 1]
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1

        # slow 本身就是有效长度（也是下一个写入位置）
        return slow


if __name__ == "__main__":
    # 你可以在本地做简单自测
    # s = Solution()
    # arr1 = [1, 1, 2]
    # k1 = s.removeDuplicates(arr1)
    # print(k1, arr1[:k1])  # 期望: 2 [1, 2]
    #
    # arr2 = [0,0,1,1,1,2,2,3,3,4]
    # k2 = s.removeDuplicates(arr2)
    # print(k2, arr2[:k2])  # 期望: 5 [0,1,2,3,4]
    pass
