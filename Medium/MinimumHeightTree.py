from collections import defaultdict
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
graph = defaultdict(list)
degree =[ 0 for i in edges]
leaves =[]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

    degree[u]+=1
    degree[v]+=1

for i in degree:
    if i == 1:
        leaves.append(i)

new_leaves =[]

# while n>2:
#     n = n - len(leaves)