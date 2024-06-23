class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # input [1,2,3]
        # make them into one integer
        # increase by one
        # make them as array again

        whole_number_str = ''.join(map(str, digits))
        whole_number_int = int(whole_number_str)

        whole_number_int += 1

        whole_number_increased_str = str(whole_number_int)
        result = [int(char) for char in whole_number_increased_str]

        return result  # output[1,2,4]
