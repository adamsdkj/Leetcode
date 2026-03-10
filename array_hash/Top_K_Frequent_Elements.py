from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for value in nums:
            result[value] = 1 + result.get(value, 0)
        arr = Solution.insertion_sort(list(result.items()))
        final = list()
        if len(arr) < k:    
            k = len(arr)
            for _ in range(k):
                final.append(arr[_][0])
        else:
            for _ in range(k):
                final.append(arr[_][0])
        return sorted(final)

    def insertion_sort(arry: List) -> List:
        for index in range(1, len(arry)):
            index2 = index - 1
            for number in arry[index2::-1]:
                if arry[index][1] > number[1]:
                    tmp = number
                    arry[index2] = arry[index]
                    arry[index] = number
                    index = index2
                index2 -= 1
        return arry

if __name__ == "__main__":
    s = Solution()
    nums=[-1, -1]
    k = 2
    print(s.topKFrequent(nums, k))
