class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
               nums[i]=0
        for i in range(len(nums)):
             v=abs(nums[i])
             if 1<=v<=len(nums):
                
                if nums[v-1]>0:
                    nums[v-1]*=-1
                elif nums[v-1]==0:
                    nums[v-1]=-1*(len(nums)+1)
        for i in range(1, len(nums)+1):
            if nums[i-1]>=0:
                return i
        return len(nums)+1