from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3, 4, 5, 6], 7))
