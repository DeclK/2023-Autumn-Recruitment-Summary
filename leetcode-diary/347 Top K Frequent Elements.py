from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        top_k = counter.most_common(k)
        return [obj[0] for obj in top_k]

test = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(test.topKFrequent(nums, k))