#DP2를 메모이제이션이 아닌 재귀함수를 통해 구현한 함수
list = [2,9,4,5,1,6,10]
def solution(i):    #n = 몇 번째 발판까지 갈 것인가
    if i ==0:
        return 0
    res = 1000
    res=min(res, solution(i-1) + abs(list[i]-list[i-1]))
    if i>1:
        res=min(res, solution(i - 2) + abs(list[i] - list[i - 2]))
    return res

print(solution(3))

a=[]
for i in range(len(list)):
    a.append(solution(i))
print(a)