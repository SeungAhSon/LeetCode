# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        temp = 0
        ans = ListNode(0)
        curr = ans
        while l1!=None or l2!=None or temp!=0:
            temp += (l1.val if l1 else 0)+(l2.val if l2 else 0)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr.next = ListNode(temp%10)
            curr = curr.next
            temp//=10
            
        return ans.next