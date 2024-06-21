class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # given string of words and spaces
        # return length of the last word

        # reverse a string
        # create a variable length=0
        # loop over, and if character != to " " (space), increase length by 1

        # before that, check if there are spaces in the given string, if not: return length of the string

        length = 0
        s = s[::-1]  # reversed
        # should remove every duplicates of spaces, because it can contain more than one
        s = " ".join(s.split())
        if " " in s:  # checking if there are any spaces in the string
            for ch in s:  # looping over the string
                if ch != " ":  # if character is not a space, increase length by 1
                    length += 1
                else:
                    return length  # if character is space, immediately return length without adding anything to it
        elif s == 0:  # check if string is not empty, if so, return none
            return None
        else:
            # if there are no spaces (meaning there is only one word) in the string, return length of the string.
            return len(s)
