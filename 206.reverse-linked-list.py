#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # In the reversed list
        # the last pointer is null hence the node before the current first will be null
        prev = None
        curr = head

        # If the next node to be reversed (curr) does not exist 
        # it means that curr is the last node in the list
        while curr is not None:
            # shift all pointers by one to the right (next)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

            # Check that the next node does exist
            # to prevent AttributeError
            if next is not None: next = curr.next

        return prev

# @lc code=end

