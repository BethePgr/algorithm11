
a=[[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]] #a의 처음항은 무게 두번째항은 값어치
k=9 #무게
list = [[0] * (k+1) for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    weight = a[i - 1][0]
    value = a[i - 1][1]
    for j in range(1,k+1):
        if j<weight:
            list[i][j] = list[i-1][j]
        else:
            list[i][j] = max(list[i-1][j-weight] + value,list[i-1][j])
print(list)
