# 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new sorted list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list/
# class ListNode:
    # def __init__(self, val = 0, next =None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: Listnode, l2: Listnode) -> ListNode:

        # make a dummy node
        dummy = ListNode()
        tail = dummy 

        # while neither l1 and l2 are not null
        while l1 and l2:
            # if left node is less than right node --> add in the left node.
            # then the left node will be the node that came after the original left node, as we already added in left node into result list.
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                # if l2 is less than l1, then add in l2, and now l2 becomes the next l2 node. 
                tail.next = l2
                l2 = l2.next
            
            # after every addition of a node to the result list, need to increment the tail variable,
            #  so that the newly added node is the new tail, and not the second last item.
            # need to update the tail variable as well.
            tail = tail.next

            # when either l1 or l2 are null: --> if only 1 is true, then the other is not
                # ALREADY PASSED THROUGH THE WHILE LOOP THAT CHECKED ONLY RUNS WHEN BOTH ARE NOT NULL
                # SO NOW, ONE OF THEM HAS TO BE NULL
            
            # if l1 is not null l2 is null
            
            # if one is null, then just add the remaining nodes in l1 to the tail of the result list, since already sorted.
            # adding the entire list1 or list2, and don't have to 1 by 1.
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2

            # dummy  
            return dummy.next
