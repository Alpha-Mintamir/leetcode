# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        curr = head
        while curr.next.next:
            curr = curr.next
        last_node = curr.next 
        curr.next = None      
        last_node.next = head.next
        head.next = last_node
        self.reorderList(head.next.next)
        return head
        



        

        