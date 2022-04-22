# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        before_nth_node = None
        nth_node = head 
        after_nth_node = nth_node.next
        pointer = head 
        node_count = 1 
        while pointer != None: 
            pointer = pointer.next 
            if node_count > n:
                before_nth_node = nth_node
                nth_node = nth_node.next
                after_nth_node = nth_node.next
            node_count += 1 
        if before_nth_node:
            before_nth_node.next = after_nth_node
        if nth_node == head:
            if before_nth_node == None and after_nth_node == None: 
                return None 
            if before_nth_node: 
                before_nth_node.next = after_nth_node 
                return head 
            else: 
                return after_nth_node
        return head