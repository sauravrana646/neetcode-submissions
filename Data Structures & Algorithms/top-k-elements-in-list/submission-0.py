class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        freq_map = defaultdict(int)
        for i in nums:
            freq_map[i] += 1
        
        for i in range(k):
            maxkey = max(freq_map,key=freq_map.get)
            final.append(maxkey)
            freq_map.pop(maxkey)
        
        return final
