from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dict() 
        result = dict()
        
        for number in nums:
            if hash_map.get(str(number), 0) == 0:
                hash_map[str(number)] = 1
            else:
                hash_map[str(number)] += 1
            if hash_map.get(str(number), 0) >= k:
                result[str(number)] = hash_map.get(str(number), 0)        
        result = sorted(result.items(), key=lambda x: x[1])
        return [item[0] for item in result[::-1]]


if __name__ == "__main__":
    s = Solution()
    nums=[1, 2]
    k = 2
    print(s.topKFrequent(nums, k))
