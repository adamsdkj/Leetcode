from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list() 
        added = set()

        for i, value in enumerate(strs):
            if i in added:
                continue
            group = []
            value_dict = self.fill_dict(value)

            for j, others in enumerate(strs):
                if (j not in added) and (value_dict
                   == self.fill_dict(others)):
                    group.append(others)
                    added.add(j)

            result.append(group)
        return result

    @staticmethod
    def fill_dict(word: str) -> Dict:
        rs = dict()
        for c in word:
            rs[c] = rs.get(c, 0) + 1
        return rs
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = tuple(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(s.groupAnagrams(strs))
    print(s.groupAnagrams2(strs))
