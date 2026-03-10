from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = str()
        for s in strs:
            added = f"#{chr(0)}{s}"
            result += added
        return result

    def decode(self, s: str) -> List[str]:
        res = s.split(f"#{chr(0)}")
        if len(res) == 0:
            return ["#"]
        return res[1:]

if __name__ == "__main__":
    s = Solution()
    tryss = ["" ,""]
    print(tryss == s.decode(s.encode(tryss)))