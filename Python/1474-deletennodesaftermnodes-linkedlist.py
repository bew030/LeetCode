class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        curr_node = head
        last_m_node = head 
        
        last_m_node = curr_node 
        #print(curr_node, last_m_node)
        last_m_node = curr_node 
        curr_node = curr_node.next
        #print(curr_node, last_m_node)
        
        '''
        while curr_node != None: 
            m_iterator = 0 
            n_iterator = 0 
            while (curr_node != None and m_iterator < m):
                last_m_node = curr_node
                curr_node = curr_node.next 
                m_iterator += 1 
            while (curr_node != None and n_iterator < n): 
                print(last_m_node)
                print()
                curr_node = curr_node.next
                n_iterator += 1 
            
            last_m_node.next = curr_node 
        '''
        '''
        m_iterator = 0 
        n_iterator = 0 
        while head != None: 
            if m_iterator < m: 
                m_iterator += 1 
                head = head.next
            else:
                node_placeholder = head
                while node_placeholder != None and n_iterator < n: 
                    node_placeholder = node_placeholder.next
                    n_iterator += 1 
                head.next = node_placeholder
                n_iterator = 0 
                m_iterator = 0 
                head = head.next
        '''
        return head