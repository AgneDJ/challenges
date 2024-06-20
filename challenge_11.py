class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # input sorted_array=[], target_value=x
        # output if target found return index. if not return index where it would be inserted in order

        for i, number in enumerate(nums):
            if number == target:
                return i
            elif target not in nums:
                nums.append(target)
                nums = sorted(nums)
                return nums.index(target)
        # runtime complexity is 0(n(log n))
        # need to use binary search
