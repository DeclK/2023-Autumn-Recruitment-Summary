from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {key: [] for key in range(numCourses)}
        in_edge = [0] * numCourses  # to find no_request courses easily
        visited = [0] * numCourses  # to log if this course visited
        # build topology
        for course, pre in prerequisites:
            d[pre].append(course)
            in_edge[course] += 1 

        # remove inedge iteratively, bfs
        import collections
        no_request = collections.deque([idx for idx in range(numCourses) if in_edge[idx] == 0])
        while len(no_request) > 0:
            course = no_request.popleft()
            visited[course] = 1

            for after_course in d[course]:
                in_edge[after_course] -= 1
                if in_edge[after_course] == 0:
                    no_request.append(after_course)
        if sum(visited) == numCourses: return True
        return False
                


test = Solution()
num = 2
l = [[1, 0]]
print(test.canFinish(num, l))