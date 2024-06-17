# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
# Each node contains a value and a reference to the next node.
# The Linked List class serves as the container for the nodes, with the head attribute pointing to the first node in the list

# checking if list1 is not empty
        if list1 == None:
            return list2
# checking if list 2 is not empty
        elif list2 == None:
            return list1

# creating dummy node (which has a listnode obj.)
        # also head. Dummy node is the first node in the list
        dummy_node = ListNode(0)
        tail = dummy_node

# creating while loop, for checking wich value is smaller, while both lists are not empty
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                # pushing list 1 before tail (because tail should be at the end)
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2  # if list2 value is smaller then list1, then dummy, list2 value, tail
                list2 = list2.next
            tail = tail.next
# checking if list1 is not empty, if it's not empty, then list1 is the tail
        if list1 != None:
            tail.next = list1
        elif list2 != None:
            tail.next = list2  # then list2 is the tail

        return dummy_node.next  # returning the head
