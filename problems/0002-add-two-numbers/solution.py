# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 342 + 465 = 7, 0 & carry=1, 7 + carry=1 -> 8
        node = ListNode(0, None)
        head = node
        carry = None

        while l1 and l2:
            ans = l1.val + l2.val
            if carry:
                ans+=carry
            if ans > 9:
                carry = ans//10
                ans = ans % 10
            else:
                carry = None

            node.next = ListNode(ans, None)

            l1=l1.next
            l2=l2.next
            node=node.next
        
        # if the length of l1 and l2 are not the same
        # add whatever left from whatever linkedlist to the node.next
        node.next = l1 or l2
        while node.next and carry:
            node=node.next
            node.val+=carry
            if node.val > 9:
                carry = node.val//10
                node.val = node.val % 10
            else:
                carry = None
        
        if carry:
            node.next=ListNode(carry, None)

        return head.next
        
