#!/usr/bin/env python3

def read_graph():
    with open("rosalind_ts.txt") as f:
        lines = f.readlines()
        # remove empty lines
        lines = [line for line in lines if line.strip()]

    n, e = map(int, lines[0].split())
    from_lists = [set() for _ in range(n)]
    to_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, lines[_+1].split())
        from_lists[v2 - 1].add(v1 - 1)
        to_lists[v1 - 1].append(v2 - 1)
    return from_lists, to_lists

def dfs(from_lists, to_lists, visited, sequence, v):
    visited[v] = True
    sequence.append(v)
    for adj in to_lists[v]:
        if not visited[adj]:
            from_lists[adj].remove(v)
            if len(from_lists[adj]) == 0:
                dfs(from_lists, to_lists, visited, sequence, adj)

def topological_sort(from_lists, to_lists):
    visited = [False] * len(from_lists)
    sequence = []
    for i in range(len(visited)):
        if not visited[i] and len(from_lists[i]) == 0:
            dfs(from_lists, to_lists, visited, sequence, i)
    return sequence

def main():
    print(' '.join(map(lambda v: str(v + 1), topological_sort(*read_graph()))))

if __name__ == '__main__':
    main()