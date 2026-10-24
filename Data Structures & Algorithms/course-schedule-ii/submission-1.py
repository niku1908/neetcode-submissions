class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        state = [0]*numCourses
        mapping = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            mapping[i].append(j)
        ans = []
        def has_cycle(course):
            if state[course]==1:
                return True

            if state[course]==2:
                # ans.append(course)
                return False

            state[course]=1

            for i in mapping[course]:
                if has_cycle(i):
                    return True

            ans.append(course)
            state[course]=2
            return False
            


        for i in range(numCourses):
            if has_cycle(i):
                return []

        return ans

        