class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        sum = bin(int(a, 2) + int(b, 2))
        sum = sum[2:]

        return sum
