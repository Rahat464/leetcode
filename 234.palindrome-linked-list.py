#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = f = head

        # Find the middle value
        # f moves 2x as fast, so when f reaches the end 
        # s will be in the middle
        while f and f.next:
            s = s.next
            f = f.next.next

        # Reverse linked list s.next to the end
        #set prev/curr.next as none so that the middle value doesnt cycle to itself
        prev = None
        curr = s
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Compare both sub linked lists
        while prev:
            if head.val != prev.val: return False
            head = head.next
            prev = prev.next
        
        return True

# @lc code=end
