from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result, added = list(), list()
        i, index = 0, 0
        for i, value in enumerate(strs):
            if i in added:
                continue
            result.append(list())
            value_dict = self.fill_dict(value)
            for j, rest_value in enumerate(strs):
                if (j not in added) and (value_dict
                   == self.fill_dict(rest_value)):
                    result[index].append(rest_value)
                    added.append(j)
            index += 1
        return result

    @staticmethod
    def fill_dict(word: str) -> Dict:
        rs = dict()
        for chr in word:
            if chr in rs:
                rs[chr] += 1
                continue
            rs[chr] = 1
        return rs


if __name__ == "__main__":
    s = Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(s.groupAnagrams(strs))
