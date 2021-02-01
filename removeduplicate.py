# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = unique =ListNode(0)
        
        if not head:
            return None
        if head and not head.next:
            return head
        if head.next and head.val != head.next.val:
            unique.next = ListNode(head.val)
            unique = unique.next
            
        while head:
            if head.next and head.val != head.next.val and (head.next.next and head.next.val != head.next.next.val or not head.next.next):
                unique.next = ListNode(head.next.val)
                unique = unique.next
            head = head.next
            
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:        
        
        if not head:
            return None
        if not head.next:
            return head


        self.new_head = None
        self.write_node = None
        
        prev = None        
        node = head

        while node:
            # look back and forward
            if (prev == None or node.val != prev.val) and \
               (node.next == None or node.val != node.next.val):
                # print(node.val)
                if not self.new_head:
                    self.new_head = node
                    self.write_node = node
                else:
                    self.write_node.next = node
                    self.write_node = node
            else:
                if self.write_node:
                    self.write_node.next = None
            prev = node
            node = node.next
        
        return self.new_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = curr = ListNode(0)
        curr.next = head
        while curr and curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                val = curr.next.val
                tmp = curr.next
                while tmp and tmp.val == val:
                    tmp = tmp.next
                curr.next = tmp
            else:
                curr = curr.next
        return ans.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        duplicate_list = set() # contain single elements
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                duplicate_list.add(cur.val)
            cur = cur.next
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            if cur.next.val in duplicate_list:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next