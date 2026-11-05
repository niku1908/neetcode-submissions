class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a, max_b, max_c = 0,0,0
        for i,j,k in triplets:
            if i>target[0] or j>target[1] or k>target[2]:
                continue

            max_a = max(max_a, i)
            max_b = max(max_b, j)
            max_c = max(max_c, k)

            if target == [max_a, max_b, max_c]:
                return True

        return False
            