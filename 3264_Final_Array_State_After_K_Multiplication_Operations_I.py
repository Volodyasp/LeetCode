import heapq
from typing import List

class Solution:
    def create_heap(self, nums: List[int]):
        hp = []
        for i, item in enumerate(nums):
            heapq.heappush(hp, [item, i])
        return hp

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hp = self.create_heap(nums)
        
        for i in range(k):
            lowest_item = heapq.heappop(hp)
            lowest_item[0] *= multiplier
            nums[lowest_item[1]] *= multiplier
            heapq.heappush(hp, lowest_item)
        
        return nums
