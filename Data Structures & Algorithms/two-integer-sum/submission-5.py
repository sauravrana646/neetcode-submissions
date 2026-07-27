class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
            
                    
        return result




        # corr = []
        # result = []
        # for i in nums:
        #     corr.append(target-i)
        # for i in range(int(len(corr)+1/2)):
        #     if corr[i] in nums and corr[i] != nums[i]:
        #         result.append(i)
        # return result