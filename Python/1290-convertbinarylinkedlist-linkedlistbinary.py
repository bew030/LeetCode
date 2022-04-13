# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        list_nums = []
        while head != None: 
            list_nums.append(head.val)
            head = head.next
        total_sum = 0 
        for i in range(len(list_nums)): 
            total_sum += list_nums[i] * (2**(len(list_nums)-1-i))
        return total_sum