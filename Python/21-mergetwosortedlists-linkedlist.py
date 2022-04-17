# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        
        p1 = list1
        p2 = list2 
        merged_list = ListNode()
        p3 = merged_list
        
        while p1 != None or p2 != None: 
            if p1 == None: 
                p3.val = p2.val
                p3.next = p2.next
                p2 = None 
            elif p2 == None:
                p3.val = p1.val
                p3.next = p1.next
                p1 = None 
            elif p1.val < p2.val: 
                p3.val = p1.val 
                new_node = ListNode()
                p3.next = new_node
                p3 = p3.next
                p1 = p1.next
            else: 
                p3.val = p2.val 
                new_node = ListNode()
                p3.next = new_node
                p3 = p3.next
                p2 = p2.next
        return merged_list