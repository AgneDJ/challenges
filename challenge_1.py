class Solution(object):
    def twoSum(self, nums, target):

        dict = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in dict:
                return [dict[compliment], i]

            dict[num] = i
