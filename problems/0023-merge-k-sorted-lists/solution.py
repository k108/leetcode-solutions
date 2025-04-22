# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_lists(self, l1, l2):
        dummy_node = ListNode()
        ans = dummy_node

        while l1 and l2:
            if l1.val > l2.val:
                dummy_node.next = l2
                l2 = l2.next
            else:
                dummy_node.next = l1
                l1 = l1.next
            dummy_node = dummy_node.next
        
        if l1:
            dummy_node.next = l1
        else:
            dummy_node.next = l2

        # excluding the dummy node
        return ans.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Time complexity: O(nlogk)
        Space complexity: O(n)
        '''
        # Check if the list of linked lists is empty or None
        if not lists or len(lists) == 0:
            return None

        # Continue merging lists until only one list remains
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp

        return lists[0]

