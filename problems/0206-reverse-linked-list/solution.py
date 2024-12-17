# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev_node=None
        current_node=head
        while current_node:
            # save next node
            next_node = current_node.next
            # change next pointer of current node to prev_node
            current_node.next = prev_node
            # change previous node to current node
            prev_node = current_node
            # assign next_node to current node
            current_node = next_node

        # return previous node as current node is None
        return prev_node
