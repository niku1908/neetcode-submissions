class Solution:

    def solve2(self, heights):

        temp =[]
        n = len(heights)
        stack=[-1]
        for i in range(n):

            while(stack[-1]!=-1 and heights[stack[-1]]>=heights[i]):
                stack.pop()

            temp.append(stack[-1])
            stack.append(i)

        return temp

    def solve1(self, heights):

        temp =[]
        n = len(heights)
        stack=[-1]
        for i in range(n-1,-1,-1):

            while(stack[-1]!=-1 and heights[stack[-1]]>=heights[i]):
                stack.pop()

            temp.append(stack[-1])
            stack.append(i)
        temp.reverse()
        return temp

    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_smaller = self.solve2(heights)

        next_smaller = self.solve1(heights)

        area = 0
        for i in range(len(heights)):
            if next_smaller[i]==-1:
                next_smaller[i]=len(heights)

            area = max(area, (heights[i]*(next_smaller[i]-prev_smaller[i]-1)))

        return area