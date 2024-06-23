class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # input [1,2,3]
        # make them a one integer
        # increase by one
        # make them as array again

        whole_number_str = str(digits)
        whole_number_one_str = whole_number_str.replace(",", "")

        whole_number_int = int(whole_number_one_str)
        whole_number_int_increased = whole_number_int + 1
        whole_number_increased_str = str(whole_number_int_increased)

        x = whole_number_increased_str.split(',')

        return increased_digits
