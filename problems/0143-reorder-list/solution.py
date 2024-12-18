# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        Time Complexity : O(n)
        Space Complexity : O(1)
        """

        # 1->2->3->4->5
        # locate mid point
        # 1->2->3 | 4->5
        # reverse second half
        # 1->2->3 | 5->4
        # 1->5
        # 2->4
        # 3
        # update linkages
        # 1->5->2->4->3

        if not head:
            # Quick response for empty linked list
            return

        # 1. locate mid point
        slow = head
        fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        mid=slow

        # 2. reverse second half
        prev_node=None
        current_node=mid
        while current_node:
            # save next node
            next_node = current_node.next
            # change next pointer of current node to prev_node
            current_node.next = prev_node
            # change previous node to current node
            prev_node = current_node
            # assign next_node to current node
            current_node = next_node
        
        head_of_second_rev = prev_node

        # 3. update linkages
        first, second = head, head_of_second_rev

        while second.next:
            next_hop = first.next
            first.next = second
            first = next_hop

            next_hop = second.next
            second.next = first
            second = next_hop
        


        

        


        


        
