class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1

        area = 0

        while i<j:
            curr_area = (j-i)*(min(heights[i], heights[j]))
            area = max(area, curr_area)

            if heights[i]<heights[j]:
                i+=1

            else:
                j-=1

        return area