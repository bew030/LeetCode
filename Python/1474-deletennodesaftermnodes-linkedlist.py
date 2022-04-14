class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        curr_node = head
        last_m_node = head 
        
        
        while curr_node != None: 
            m_iterator = 0 
            n_iterator = 0 
            while (curr_node != None and m_iterator < m):
                last_m_node = curr_node # HARD COPY of the reference 
                curr_node = curr_node.next 
                m_iterator += 1 
            while (curr_node != None and n_iterator < n): 
                print(last_m_node)
                print()
                curr_node = curr_node.next
                n_iterator += 1 
            
            last_m_node.next = curr_node 
       
        return head