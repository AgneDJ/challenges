class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # haystack = "sadbutsad"
        # needle= "sad"
        # output 0

        length_needle = len(needle)
        length_haystack = len(haystack)

        # handling edge cases
        if length_needle == 0 or length_haystack == 0:  # if empty, return -1
            return -1

        elif length_haystack < length_needle:  # if needle is longer, return -1
            return -1

        # loop over haystack string
        for letter_index in range(length_haystack - length_needle + 1):
            # checks if haystack of needle matches needle
            if haystack[letter_index:letter_index + length_needle] == needle:
                return letter_index  # if yes, then return index
        return -1  # if no, return -1
