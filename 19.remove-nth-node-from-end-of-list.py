#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        # e.g. when there is only one node in the list and it is removed
        dummy = ListNode(0)
        dummy.next = head

        # Will point to the n+1th last node in the list
        prev = dummy
        count = -(n)

        # Create a pointer to the head of the list
        curr = head

        # Iterate through the list until the end is reached
        while curr:
            if count == 0: prev = prev.next
            else: count += 1
            curr = curr.next

        # Remove the nth node from the end of the list
        prev.next = prev.next.next
        
        return dummy.next

# @lc code=end

