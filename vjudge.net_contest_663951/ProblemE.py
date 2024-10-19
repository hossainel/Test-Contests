# author @kento_kun
N, M, Q = map(int, input().split())

INF = 1e+18
edges_all = []
costs = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    costs[a][b] = c
    costs[b][a] = c
    edges_all.append((a, b, c))

for n in range(N):
    costs[n][n] = 0

query_list = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b, c = edges_all[query[1] - 1]
        costs[a][b] = INF
        costs[b][a] = INF
    
    query_list.append(query)

query_list = query_list[::-1]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if costs[i][k] != INF and costs[k][j] != INF:
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

ans_list = []
for query in query_list:
    if query[0] == 2:
        ans = costs[query[1]-1][query[2]-1]
        if ans == INF:
            ans = -1
        ans_list.append(ans)
    else:
        u, v, c = edges_all[query[1] - 1]
        for a in range(N):
            for b in range(N):
                costs[a][b] = min(costs[a][b], costs[a][u] + c + costs[v][b], costs[a][v] + c + costs[u][b])

ans_list = ans_list[::-1]
for ans in ans_list:
    print(ans)
