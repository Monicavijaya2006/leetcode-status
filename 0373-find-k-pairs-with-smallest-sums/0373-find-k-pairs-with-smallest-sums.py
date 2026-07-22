class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(min(k , len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while heap:

            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if len(ans) == k : return ans

            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return ans

