# DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class Dijkstra:

    def Dijkstra_alg(self, n, e, mat, s):
        # Write your code here to calculate shortest paths and usp values from source to all vertices
        # This method will have four inputs (Please see testcase file)
        # This method should return a two dimensional array as output (Please see testcase file)

        # initialization
        vertices = [i for i in range(1, n+1)]
        distences = {v: float('inf') for v in vertices}
        distences[s] = 0
        queue = sorted([[k, v]
                        for k, v in distences.items()], key=lambda x: x[1])
        weights = {}
        for m in mat:
            weights[(m[0], m[1])] = m[2]
            weights[(m[1], m[0])] = m[2]
        graph = {v: [] for v in vertices}
        for m in mat:
            graph[m[0]].append(m[1])
            graph[m[1]].append(m[0])
        S = [False] * (n + 1)
        usp = [None] * (n + 1)
        usp[s] = 1

        # Run Dijkstra
        while queue:
            element = queue.pop(0)
            u = element[0]
            S[u] = True
            for v in graph[u]:
                # Run Relax
                if not S[v]:
                    temp_dist = distences[u] + weights[u, v]
                    if temp_dist < distences[v]:
                        distences[v] = temp_dist
                        usp[v] = usp[u]
                    elif temp_dist == distences[v]:
                        usp[v] = 0
            # Update queue
            for q in queue:
                if distences[q[0]] < q[1] and not S[q[0]]:
                    q[1] = distences[q[0]]
            queue = sorted(queue, key=lambda x: x[1])

        ans = []
        for k, v in distences.items():
            ans.append([v, usp[k]])
        return ans
