class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            mapping[course].append(pre)

        state = [0]*numCourses

        def has_cycle(i):
            if state[i]==1:
                return True
            if state[i]==2:
                return False

            state[i]=1

            for pre in mapping[i]:
                if has_cycle(pre):
                    return True
            state[i]=2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True