# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def count_nodes(head):
            curr = head
            count = 0
            while curr:
                count += 1
                curr = curr.next

            return count

        if not head:
            return head
        num = count_nodes(head)
        mid = (num // 2) + 1 
        curr = head
        count = 1

        while count < mid:
            count += 1
            curr = curr.next

        return curr

# O(N), n being the size of list        
# 
# 
#         
# 
# 
