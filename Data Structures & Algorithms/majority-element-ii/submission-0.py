class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq={}
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num, count in freq.items():
            if count>n//3:
                res.append(num)
        return res