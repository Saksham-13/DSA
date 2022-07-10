class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = nums[0]
        l= len(nums) 
        if(len(nums)==1):
            return 1
        i=1
        while(i <l):
            
            if(nums[i]==c):
                nums.remove(nums[i])
                
                l=l-1
                continue
            else:
                c = nums[i]
                i=i+1
        return len(nums)
            
            