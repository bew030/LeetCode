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
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head 
        fast_pointer = head
        
        while fast_pointer and fast_pointer.next: # made it to the last node OR past the last node 
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer
'''