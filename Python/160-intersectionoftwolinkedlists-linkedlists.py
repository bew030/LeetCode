# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # create dictionary of nodes and their self.next value, then iterate through the next linked list and see if their 
        # values are the same 
        
        # Solution 1: calculate length of both lists, find minimum length, shorten the longest list to the minimum length
        # (keeping the LAST n nodes where n is the minimum), then loop through the unshortened list and shortened list and 
        # see if they're equal. If they both reach the end and are NOT equal, return None. 
        # This is built on the premise that if there are duplicates then it must be near the end and is at most n nodes where 
        # n is the shorter length. 
        
        len_a = 0 
        len_b = 0
        
        iter_a = headA
        iter_b = headB
        
        while iter_a != None: 
            len_a += 1 
            iter_a = iter_a.next
        while iter_b != None: 
            len_b += 1 
            iter_b = iter_b.next
        
        min_len = 0 
        if len_a < len_b:
            min_len = abs(len_b-len_a)
            decrease_size = headB
            stays = headA
        else: 
            min_len = abs(len_b-len_a)
            decrease_size = headA
            stays = headB
            
        iterator = 0
        while iterator < min_len: 
            decrease_size = decrease_size.next
            iterator += 1 
        
        while stays != None and decrease_size != None:
            if stays == decrease_size:
                return stays 
            else: 
                stays = stays.next
                decrease_size =decrease_size.next
        return None
        
        '''
        # Solution 2: Iterate through the first list and add each node in a set. Then iterate through the second list and 
        # check if the node is in the set. If you iterate through the entire second list and don't see any nodes, return
        # None. 
        
        set_next_nodes = set()
        
        a_iter = headA
        while a_iter != None: 
            set_next_nodes.add(a_iter)
            a_iter = a_iter.next
        
        b_iter = headB
        while b_iter != None: 
            if b_iter in set_next_nodes: 
                return b_iter 
            b_iter = b_iter.next
        return None
        '''
        
        '''
        # Solution 3: This was their genius code to have one pointer measure the length of the longer list and another
        # pointer measure the shorter list and then placing it on the longer list. Then both steps are stepping through the 
        # list at the same time. TRY TO UNDERSTAND THIS CODE. 
        
        pA = headA
        pB = headB

        while pA != pB:
            if pA is None: 
                pA = headB 
            else: 
                pA = pA.next
            if pA is None:
                print(pA)
            else:
                print(pA.val)
                
            if pB is None: 
                pB = headA
            else: 
                pB = pB.next
            if pB is None:
                print(pB)
            else:
                print(pB.val)
            print()
        return pA
        '''