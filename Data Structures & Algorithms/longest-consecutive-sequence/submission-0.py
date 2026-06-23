class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            lenght = 1
            if nums[i]-1 not in numsSet:
                n = nums[i]
                while n+1 in numsSet:
                    lenght+=1
                    n+=1
           
            longest = max(longest, lenght)

        return longest
