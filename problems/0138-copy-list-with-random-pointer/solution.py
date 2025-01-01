"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''

        '''
        Approach :-

        1. Interweave the nodes of the old and copied list. 
        For example: Old List: A --> B --> C --> D 
        InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'

        Use interweaved structure to get the correct reference nodes for random pointers.

        2. Just iterate the linked list and create copies of the nodes on the go. 
        Since a node can be referenced from multiple nodes due to the random pointers, 
        ensure you are not making multiple copies of the same node.
        
        Use extra space to keep old_node ---> new_node mapping 
        to prevent creating multiple copies of the same node.

        '''
        dummy_node = Node(x=0)
        new_head = dummy_node

        if not head:
            return None

        old_new_mapping = {}

        while head:
            val = head.val
            random = head.random

            new_node = Node(x=val, random=random)
            new_head.next = new_node
            old_new_mapping[head]=new_node

            new_head = new_head.next
            head = head.next

        new_head = dummy_node

        while new_head:
            if new_head.random:
                new_head.random=old_new_mapping[new_head.random]
            new_head = new_head.next

        return dummy_node.next

        


        
