class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        possible_parentheses = {')': '(', ']': '[', '}': '{'}  # dictionary
        empty_list = []  # for checking

        for ch in s:  # loop over s
            if ch in possible_parentheses:
                if empty_list is not 0 and empty_list[-1] == possible_parentheses[ch]:
                    empty_list.pop()
                else:
                    return False
            else:
                empty_list.append(ch)

        return True
