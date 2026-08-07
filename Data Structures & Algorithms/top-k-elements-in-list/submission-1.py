class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        freq_map = defaultdict(int)
        for i in nums:
            freq_map[i] += 1
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for key,value in freq_map.items():
            buckets[value].append(key)
        
        for freq in range(n,0,-1):
            for num in buckets[freq]:
                if len(final) < k:
                    final.append(num)
                else:
                    break

        return final