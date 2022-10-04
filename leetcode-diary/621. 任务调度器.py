from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counter = Counter(tasks)
        task_num = len(tasks)
        task, num = counter.most_common(1)[0]
        max_volume = num * (n + 1)
        if task_num <= max_volume:
            max_count = sum([1 if val == num else 0 \
                                for val in counter.values()])
            rest_task = task_num - max_count * num
            end = max(0, rest_task - (n + 1 - max_count) * (num - 1))
            return (num - 1) * (n + 1) + max_count + end
        return task_num
        

test = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]; n = 2
print(test.leastInterval(tasks, n))