import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    cnt=0
    total=0

    for i in range(n):
        while True:
            if cnt==m or A[i]<=B[cnt]:
                total+=cnt
                break
            else:
                cnt+=1
                
    print(total)