import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def preorder(i_start, i_end, p_start, p_end):
    if i_start > i_end or p_start > p_end:
        return
    
    root = postorder[p_end]
    idx = node_index[root]
    left_len = idx - i_start

    print(root, end=' ')

    preorder(i_start, idx - 1, p_start, p_start + left_len - 1)
    preorder(idx + 1, i_end, p_start + left_len, p_end - 1)

n = int(input())
inorder = list(map(int, input().split())) # 중위
postorder = list(map(int, input().split())) # 후위

node_index = [-1] * (n+1)
for i in range(n):
    node_index[inorder[i]] = i

preorder(0, n-1, 0, n-1)