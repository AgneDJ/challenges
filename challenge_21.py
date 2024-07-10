# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        def check(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (left.val == right.val) and check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right)
