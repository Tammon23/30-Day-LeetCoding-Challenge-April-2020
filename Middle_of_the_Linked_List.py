class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        midNode = head
        
        
        # apparently for loops are faster than while loops in python, so i changed it to do less stuff in the while loop
#         nodesPassed = 0
#         while(head):
#             nodesPassed += 1
#             if nodesPassed % 2 == 0:
#                 midNode = midNode.next
                
#             head = head.next

        
        listLen = 0
        while(head):
            listLen += 1
            head = head.next
            
        for i in range(listLen):
            if listLen//2 == i:
                return midNode
            midNode = midNode.next
            
        
                    
            
        
