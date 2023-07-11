#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:     
        # Floyd's tortoise and hare algorithm
        # The hare is twice as fast as the tortoise
        # If the list is cyclical, the hare will reach it first
        # If cyclical, the tortoise and hare will eventually meet
        
        # Both pointers start at the head
        t, h = head, head

        # Check that the hare node is not Null
        # Also check its next node to prevent NoneType error
        while h and h.next:
            t = t.next
            h = h.next.next

            if t==h:
                return True
        
        return False

        
        
# @lc code=end

