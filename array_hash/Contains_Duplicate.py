from typing import List


class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, value in enumerate(nums):
            if value in nums[index + 1:]:
                return True
        return False

    def hasDuplicate2(self, nums: List[int]) -> bool:
        hash_set = set()
        for value in nums:
            if value in hash_set:
                return True
            hash_set.add(value)
        return False


if __name__ == "__main__":
    test_case = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 1, 2, 3, 4, 5, 6],
        [0, 2, 4]
    ]
    solution = Solution()
    for index in range(test_case.__len__()):
        print(f"index: {index}, test case: {test_case[index]}"
              f" result: {solution.hasDuplicate(test_case[index])}")
