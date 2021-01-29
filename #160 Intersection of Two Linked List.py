
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        arr=[]
        
        if(not headA or not headB):return None
        else:
            A_pointer=headA
            B_pointer=headB
            
            while(A_pointer!=B_pointer):
                A_pointer=headB if A_pointer==None else A_pointer.next
                B_pointer=headA if B_pointer==None else B_pointer.next
                
            return A_pointer
            
            
