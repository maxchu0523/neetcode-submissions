class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        last = defaultdict(int)
        last[0] = 1
        for n in nums:
            curr = defaultdict(int)
            for lastVal, count in last.items():
                plus = lastVal + n
                minus = lastVal - n
                curr[plus] += last[lastVal]
                curr[minus] += last[lastVal]
            print(curr)
            last = curr

        return curr[target]