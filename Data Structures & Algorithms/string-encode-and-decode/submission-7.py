class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr < len(s):
            count = ""
            while s[curr] != "#":
                count += s[curr]
                curr += 1

            count = int(count)
            curr += 1
            res.append(s[curr:curr+count])
            curr += count 
        return res
