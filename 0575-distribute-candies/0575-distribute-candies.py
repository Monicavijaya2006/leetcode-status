class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set(candyType)
        h = int(len(candyType) / 2)
        if len(s) == h or len(s) > h:
            return h
        elif len(s) < h:
            return len(s)
        