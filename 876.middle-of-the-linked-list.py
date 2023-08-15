#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's tortoise and hare algorithm
        # The hare is twice as fast as the tortoise

        # Both pointers start at the head
        t, h = head, head

        # Hare will reach the end first since it goes twice as fast.
        # Keep going until hare reaches the end
        while h and h.next:
            t = t.next
            h = h.next.next

        return t

        
# @lc code=end

