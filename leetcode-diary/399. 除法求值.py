from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        import collections
        d = collections.defaultdict(list)
        for (x, y), value in zip(equations, values):
            d[x].append((y, value))
            d[y].append((x, 1 / value))

        def dfs(node, target, ans, visit):
            if node == target:
                return ans
            if visit[node]:
                return None
            visit[node] = True
            ret = None
            for next_node, value in d[node]:
                ret = dfs(next_node, target, ans * value, visit)
                if ret is not None:
                    break
            visit[node] = False
            return ret
            
        nodes = d.keys()
        visit = {node: False for node in nodes}
        rets = []
        for x, y in queries:
            if x not in d.keys() or y not in d.keys():
                rets.append(-1)
                continue
            ret = dfs(x, y, 1, visit)
            if ret is not None:
                rets.append(ret)
            else:
                rets.append(-1)

        return rets

test = Solution()
equations = [["a","b"],["b","c"]];values = [2.0,3.0];queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(test.calcEquation(equations, values, queries))

                