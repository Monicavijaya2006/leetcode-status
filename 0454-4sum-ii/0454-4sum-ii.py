class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ctr = Counter([a+b for a in nums1 for b in nums2])
        return sum(ctr[-a-b] for a in nums3 for b in nums4)