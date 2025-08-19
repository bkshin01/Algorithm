import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
visited = [[triangle[0][0]] * (i+1) for i in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            visited[i][j] = visited[i-1][j] + triangle[i][j]
        elif j == i:
            visited[i][j] = visited[i-1][j-1] + triangle[i][j]
        else:
            visited[i][j] = max(visited[i-1][j-1], visited[i-1][j]) + triangle[i][j]

print(max(visited[n-1]))