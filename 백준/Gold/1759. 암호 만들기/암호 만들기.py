def dfs(idx, l, n, m, password):
    if len(password) == l:
        if n >= 1 and m >= 2:  # 모음 1개 이상, 자음 2개 이상
            print(password)
        return
    
    if idx >= len(kind):
        return

    # 현재 문자를 포함시키는 경우
    if kind[idx] in ('a', 'e', 'i', 'o', 'u'):
        dfs(idx + 1, l, n + 1, m, password + kind[idx])
    else:
        dfs(idx + 1, l, n, m + 1, password + kind[idx])
    
    # 현재 문자를 포함시키지 않는 경우
    dfs(idx + 1, l, n, m, password)

l, c = map(int, input().split())
kind = sorted(input().split())

dfs(0, l, 0, 0, "")
