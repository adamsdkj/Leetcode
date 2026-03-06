from typing import Dict


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map_s = self.fill_hash_map(s)
        hash_map_t = self.fill_hash_map(t)
        return hash_map_s == hash_map_t

    def fill_hash_map(self, s: str) -> Dict:
        hash_map = dict()
        for char in s:
            if char in hash_map.keys():
                hash_map[char] += 1
                continue
            hash_map[char] = 1
        return hash_map


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("aabc", "abcs"))
