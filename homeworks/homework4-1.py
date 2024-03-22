vert_num = 6
edge_list = [
    [0, 1], [0, 3],
    [1, 3],
    [2, 3],
    [4, 0], [4, 3],
    [5, 0]
]


adj_list = [[] for _ in range(vert_num)]
for u, v in edge_list:
    adj_list[u].append(v)

g = adj_list
parents = [None for _ in range(vert_num)]
colors = ['w' for _ in range(vert_num)]
timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]


def dfs(v, p=-1):
    global timer
    parents[v] = p
    colors[v] = 'g'
    timer += 1
    tin[v] = timer
    for u in g[v]:
        if colors[u] == 'g':
            print(f'found cycle {v} -> {u}')
            continue
        elif colors[u] == 'b':
            continue
        elif colors[u] == 'w':
            dfs(u, v)
    colors[v] = 'b'
    timer += 1
    tout[v] = timer


def top_sort():
    for v in range(vert_num):
        if colors[v] == 'w':
            dfs(v)
    vert_list = [i for i in range(vert_num)]
    ans = [
        x for y, x in sorted(zip(tout, vert_list),
        key=lambda pair: pair[0], reverse=True)
        ]
    return ans


ts = list(reversed(top_sort()))
sa1d = [1 for _ in range(vert_num)]
for i in ts:
    for j in adj_list[i]:
        sa1d[i] += sa1d[j]

print(sa1d)


def restore_cycles():
