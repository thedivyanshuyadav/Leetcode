
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(not head):return False
        else:
            cycle=False
            trav=head
            while(trav):
                if(trav.val==10**6):
                    cycle=True
                    break
                last=trav
                trav.val=10**6
                trav=trav.next
           
            return cycle
            
            
