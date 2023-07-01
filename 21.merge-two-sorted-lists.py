#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initiate new linked list
        merged_list = ListNode()
        # Initially, there are no nodes
        # so the head and tail pointer need to point to an empty linkedlist as a placeholder.
        tail = merged_list

        # Loop as long as both are not Null,
        # which means that the lists still contain nodes
        while list1 and list2:
            # Check if l1 is smaller than l2
            # In Linked Lists, it automatically assumes you're looking for the node pointed by the head
            # so there is no need to mention which node to look for.
            if list1.val < list2.val:
                # Update the next tail pointer to point to new node
                tail.next = list1
                list1 = list1.next
            
            else:
                tail.next = list2
                list2 = list2.next

            # Tail is updated to point to new last node
            tail = tail.next
        
        # If one of the lists is empty, add all the nodes from the other list to the merged list
        if list1: tail.next = list1
        elif list2: tail.next = list2

        return merged_list.next


# @lc code=end
