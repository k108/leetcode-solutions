# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummy points to the start of the result linkedlist and
        # temp is used for traversal
        dummy=temp=ListNode()

        while list1 and list2:
            # check val of each of them and 
            # add the smaller one to the result linkedlist
            if list1.val < list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next

        # if the length of l1 and l2 are not the same
        # add whatever left from whatever linkedlist to the temp.next
        temp.next = list1 or list2
        
        # we return first node that we added to the linkedlist
        return dummy.next

        
