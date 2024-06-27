# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # sorted linked list
        # currentnode is ahead
        current = head

        # ehile current node is not empty and the one after this one

        while current != None and current.next != None:
            if current.val == current.next.val:  # if current node value = next one, then skipping this node and then next one is the one after the next one now
                current.next = current.next.next
            else:
                # otherwise, current node equals next node now, and proceeding to the next node
                current = current.next

        return head  # retun new head after duplicates are removed
