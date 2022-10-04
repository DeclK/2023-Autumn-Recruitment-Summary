from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sort_people = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
        ret_queue = []
        for person, nums in sort_people:
            if nums < len(ret_queue):
                ret_queue.insert(nums, (person, nums))
            else:
                ret_queue.append((person, nums))

        return ret_queue

test = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(test.reconstructQueue(people))
