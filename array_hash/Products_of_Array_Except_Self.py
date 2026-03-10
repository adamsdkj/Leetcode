from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()
        for index in range(0, len(nums)):
            sum = 1
            for j, number in enumerate(nums):
                if j == index:
                    continue
                sum *= number
            result.append(sum)
        return result

if __name__ == "__main__":
    s = Solution()
    nums = [0, 0]
    print(s.productExceptSelf(nums))