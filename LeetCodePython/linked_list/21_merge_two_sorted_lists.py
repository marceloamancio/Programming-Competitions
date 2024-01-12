# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None

        list3, last_node = None, None
        while list1 and list2:
            list1, list2 = (list1, list2) if list1.val < list2.val else (list2, list1)
            
            if list3:
                last_node.next = list1
                last_node = last_node.next
            else:
                last_node = list1
                list3 = last_node

            list1 = list1.next

        list1 = list1 if list1 else list2
        if list1:
            if last_node:
                last_node.next = list1
            else:
                list3 = list1

        elif last_node:
            last_node.next = None

        return list3
