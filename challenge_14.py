class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    # build-in method
        # sums up two inputs a and b(which are strings), by converting them into integers (int), a - number, 2 - declare it as binary, and ten makes sum into binary
        sum = bin(int(a, 2) + int(b, 2))
        sum = sum[2:]  # removes the prefix 0b (binary prefix )

        return sum
