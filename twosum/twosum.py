class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i, j in enumerate(nums):
            tar = target - j
            if tar in d:
                return [i, d[tar]]
            else:
                d[j] = i

        return []
            
# Time complexity = O(n) -> just go through the list once
#             
# 
#         
# 
# 