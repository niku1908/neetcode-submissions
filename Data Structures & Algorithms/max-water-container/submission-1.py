class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        ans = 0

        while(i<j):
            area = (j-i)*(min(heights[i], heights[j]))
            ans = max(ans, area)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1

        return ans