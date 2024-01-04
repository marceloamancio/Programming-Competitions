# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_node = ListNode()
        current_node = first_node
        first_loop = True
        forward = 0

        while True:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + forward
            digit, forward = total % 10, total // 10

            if digit + forward == 0 and (l1 == None) and (l2 == None):
                break

            if first_loop:
                current_node.val = digit
                first_loop = False
            else:
                current_node.next = ListNode(digit)
                current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None        


        return first_node
        
