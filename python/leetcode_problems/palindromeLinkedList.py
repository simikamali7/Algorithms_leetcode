# 234. Palindrome Linked List

# given a singly linked list, determine if its a palindrome
# input = 1->2, output = false 
# input = 1->2->2->1, output = true

# array solution

# Definition for singly-linked list 
# class ListNode: 
#    def __init__(self, val = 0, next = None):
#        self.val = val
#        self.next = next

# parameters; always include self, also accepts head = a ListNode.
# returns a bool

# add all the the values in linked list into an array nums
# uses extra memory --> b/c have to initialize a list.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []

        # while haven't reached end of the list
            # add the head value to array
            # shift head pointer to the right.
        while head:
            nums.append(head.val)
            head = head.next
        
        # left pointer starts at index 0
        # right pointer starts at last index

        # while the l <= r --> condition that prevents cross over

        # if the val of the left pointer == r pointer value --> then palindrome.
            # if the val at l pointer != r pointer, return False.
            # not a palindrome
        # then increment left pointer by 1
        # decrement right pointer by 1 to the left
        # when the while condition is met, l == r, while loop doesn't run
            # return 
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
# Method 2:
# 2 pointers - 1 slow pointer, 1 fast pointer
# will use algorithm to reverse a linked list.
    # then can check if it a linked list

# can do this in O(1) memory

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # initialize both at head.
        fast = head
        slow = head

        # while fast is not null itself, and while the next value to fast is not null.
        # keep going until fast is at the last node, or has reached null.

        # will shift fast pointer 2 times
        # will shift slow pointer one at a time.

        # find middle node (where the slow pointer will be)
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next

        # REVERSE SECOND HALF OF THE LIST
            # start at slow and keep going until reach end of list
            # store next node at temp variable

        prev = None 
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # CHECK IF PALINDROME

        # if left value != right value, then not palindrome
        # else keep updating pointers and check again.
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        
        return True