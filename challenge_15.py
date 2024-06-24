class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # input 4
        # output 2
        # in 2 out 1
        # in 8 out 2
        # root = 0.5 * (X + (N / X))
        if x == 0:
            return 0

        a = x
        b = (x + 1) / 2
        while b < a:
            a = b
            b = (b + x / b) / 2

        return a
