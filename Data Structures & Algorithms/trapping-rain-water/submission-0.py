class Solution:

    def solve(self, height, left_maxi):

        left_maxi.append(0)
        for i in range(1, len(height)):
            left_maxi.append(max(left_maxi[-1], height[i-1]))

    def solve1(self, height, right_maxi):
        right_maxi.append(0)
        n = len(height)
        for i in range(n-2, -1,-1):
            right_maxi.append(max(right_maxi[-1], height[i+1]))

    def trap(self, height: List[int]) -> int:
        left_maxi = []
        right_maxi = []

        self.solve(height, left_maxi)
        self.solve1(height, right_maxi)
        right_maxi.reverse()
        ans =0  
        for i in range(len(height)):
            total = min(right_maxi[i], left_maxi[i])-height[i]
            if total<0:
                continue

            else:
                ans+=total

        return ans








