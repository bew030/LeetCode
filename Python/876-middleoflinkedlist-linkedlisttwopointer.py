# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        array_rep = []
        while head != None: 
            array_rep.append(head)
            head = head.next
        
        return array_rep[len(array_rep)//2]
        
        '''
        node_iterator = head 
        length_list = 0
        while node_iterator != None: 
            length_list += 1 
            node_iterator = node_iterator.next
        # middle = length_list//2
        
        mid_pt = length_list//2
        
        node_iterator = head 
        iterator = 0 
        
        while node_iterator != None: 
            if iterator == mid_pt: 
                return node_iterator
            node_iterator = node_iterator.next
            iterator += 1 
        '''