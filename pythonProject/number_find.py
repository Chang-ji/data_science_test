import heapq

n, m = map(int, input().split())
array = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for data_el in array[data]:
        indegree[data_el] -= 1
        if indegree[data_el] == 0:
            heapq.heappush(heap, data_el)

for i in result:
    print(i, end=" ")
