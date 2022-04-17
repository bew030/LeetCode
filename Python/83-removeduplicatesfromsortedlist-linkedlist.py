# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: 
            return head
        
        iterator = head.next
        last_non_duplicate = head 
        
        while iterator != None:
            if iterator.val == last_non_duplicate.val: 
                if iterator.next == None: 
                    last_non_duplicate.next = None
                iterator = iterator.next
            else: 
                last_non_duplicate.next = iterator 
                last_non_duplicate = iterator 
                iterator = iterator.next
                
        return head