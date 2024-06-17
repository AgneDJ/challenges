class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # #set is for removing duplicates
        # #make nums to a set
        # # return set

        # #example nums=[3,2,5,2]
        # nums = set(nums)
        # #nums=(3,2,5)
        # k = list(nums)
        # #nums=[3,2,5]

       # other solution
        k = 1  # count of unique num

        for num in range(1, len(nums)):
            # if number of nums is not == previous num... maybe count should start at 1, not 0
            if nums[num] != nums[num-1]:
                nums[k] = nums[num]
                k += 1  # add one unique
            elif len(nums) == 0:  # if nums is empty, return non
                return None

        return k
