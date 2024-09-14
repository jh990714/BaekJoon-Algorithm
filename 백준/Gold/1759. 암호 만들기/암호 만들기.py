def dfs(idx, n, m, str):
    if idx == c:
        if len(str) == l and n >= 1 and m >= 2:
            print(str)
            
        return

    if kind[idx] in vowels:
        dfs(idx + 1, n + 1, m, str + kind[idx])
    else:
        dfs(idx + 1, n, m + 1, str + kind[idx])

    dfs(idx + 1, n, m, str)
    
l, c = map(int, input().split())
kind = sorted(input().split())

result = []
vowels = ['a', 'e', 'i', 'o', 'u']

dfs(0, 0, 0, "")