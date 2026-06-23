class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(temp, options):
            print(temp)
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            
            localOptions = options.copy()
            for option in localOptions:
                temp.append(option)
                options.remove(option)
                dfs(temp, options)
                temp.pop()
                options.add(option)
        dfs([],set(nums))
        return res