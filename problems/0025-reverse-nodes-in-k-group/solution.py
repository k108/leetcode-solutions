# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check if we need to reverse the group
        # num elements < k
        curr_node = head
        for _ in range(k):
            if not curr_node:
                return head
            curr_node = curr_node.next

        # reverse the group, by simple linked list reversal
        prev_node = None
        curr_node = head
        for _ in range(k):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # post group reversal, 
        # `head` is the tail of the group, link it with the next reversed group
        # `curr_node` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr_node, k)
        
        # head node of the reversed group
        return prev_node



        

        
