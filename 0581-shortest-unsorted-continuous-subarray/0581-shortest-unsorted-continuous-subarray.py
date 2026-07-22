class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """ 
          ..
          ..
        ()@@()
          __
        """
        n=len(nums)
        l=0 
        r=n-1
        while l+1<n and nums[l]<=nums[l+1]:
            l+=1
        while r-1>=0 and nums[r]>=nums[r-1]:
            r-=1
        if l>=r:
            return 0 
        bmin=nums[l+1]
        bmax=nums[l+1]
        mxh=[]
        for i in range(l+1):
            heapq.heappush(mxh,-nums[i])
        mh=[]
        for i in range(r,n):
            heapq.heappush(mh,nums[i])
        for i in range(l+1,r):
            bmin=min(bmin,nums[i])
            bmax=max(bmax,nums[i])
        print(bmin,bmax)
        l+=1
        r-=1
        Max=-mxh[0]
        Min=mh[0]
        print(Max,Min)
        while bmin<Max or bmax>Min:
            if bmin<Max:
                if l==0:
                    break
                bmin=min(bmin,nums[l-1])
                bmax=max(bmax,nums[l-1])
                if nums[l-1]==Max:
                    heapq.heappop(mxh)
                if len(mxh):
                    Max=-mxh[0]
                else:
                    Max=float('-inf')
                l-=1
            if bmax>Min:
                if r==n-1:
                    break
                bmin=min(bmin,nums[r+1])
                bmax=max(bmax,nums[r+1])
                if nums[r+1]==Min:
                    heapq.heappop(mh)
                if len(mh):
                    Min=mh[0]
                else:
                    Min=float('inf')
                r+=1
        return r-l+1