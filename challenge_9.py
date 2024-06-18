class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = len(nums)

        new_array = []

        for num in nums:
            if num != val:
                new_array.append(num)

        nums[:] = new_array

        return k
