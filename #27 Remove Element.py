
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        while(i<n and nums):
            
            if(nums[i]==val):
                nums.pop(i)
                n-=1
            else:i+=1
        
        return len(nums)
        
        
