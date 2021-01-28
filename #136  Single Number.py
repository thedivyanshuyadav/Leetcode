
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[0]*n
        
        
        for i in range(n):
            if(arr[i]==1):continue
            a=nums[i]
            for j in range(i+1,n):
                if(nums[j]==a):
                    arr[j]=1
                    arr[i]=1
                    break
        
        return nums[arr.index(0)]
        
        
