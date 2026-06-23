class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            lenght = 0
            if nums[i]-1 not in numsSet:
                while nums[i] + lenght in numsSet:
                    lenght+=1
           
            longest = max(longest, lenght)

        return longest
