# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        a = []
        a.append(temp.val)
        while temp.next :
            a.append(temp.next.val)
            temp = temp.next

        b =''
        for i in a:
            b+=str(i)

        b = str(2*int(b))
        a.clear()
        d = []
        for i in b:
            d.append(int(i))

        head = ListNode(d.pop(0))
        temp = head

        for i in range(len(d)):
            new = ListNode(d[i])
            temp.next = new
            temp = temp.next

        return head




