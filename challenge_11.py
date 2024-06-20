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
    # binary search solution
        left = 0  # left is arrays starting point 0
        right = len(nums)-1  # right is arrays ending point len-1

        while right >= left:  # while left is not bigger than right
            middle = (left + right) // 2  # the middle is going to be avg

            if nums[middle] == target:  # checking if number in the middle equals target
                return middle  # if yes, return index of that number of the array

            elif nums[middle] < target:  # if not, and is less than target
                left = middle + 1  # index of left is now index of middle + 1

            else:
                right = middle - 1  # if not, and is more than target

        return left  # return index of left
