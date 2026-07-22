from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: 
        all_perms = list(permutations(nums)) 
        return all_perms
     