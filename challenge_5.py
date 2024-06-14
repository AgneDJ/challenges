class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500, "M": 1000}
        empty_list = []

        s = str(s)
        empty_list = []
        length = len(s)

        for i in range(length):
            current_value = roman_dict[s[i]]
            if i < length - 1 and current_value < roman_dict[s[i + 1]]:
                empty_list.append(-current_value)
            else:
                empty_list.append(current_value)

        return sum(empty_list)
