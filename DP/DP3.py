#냅색(배낭) 문제
list = [[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]]
def solution(list,k): #list는 무게가치가 있는 배열 k는 넘어서는 안되는 무게제한
    knapsack = [[0]*(k+1) for i in range(len(list)+1)]
    for i in range(1,len(list)):
        for j in range(1,k):
            knapsack[i+1][k] = knapsack[i+1][k],knapsack[i+1][k]