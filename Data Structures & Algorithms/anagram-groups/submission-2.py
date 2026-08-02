class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            hashmap = [0]*26
            for ch in word:
                hashmap[ord(ch)-ord('a')] +=1
            if tuple(hashmap) not in groups.keys():
                groups[tuple(hashmap)] = []
            groups[tuple(hashmap)].append(word)
        return list(groups.values())
          
                
