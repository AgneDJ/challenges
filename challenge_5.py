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
        for ch in s:
            for dict_ch in roman_dict:
                if ch == dict_ch:
                    empty_list.append(roman_dict[dict_ch])
        return sum(empty_list)
