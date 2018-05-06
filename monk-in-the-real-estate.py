test = int(input())

for i in range(test):
    road = int(input())
    visited = [False] * 10001
    for xy in range(road):
        x,y = map(int, input().split())
        visited[x]=True
        visited[y]=True

    count=0
    for i in range(10001):
        if(visited[i]):
            visited[i]=False
            count++
    print(count)
