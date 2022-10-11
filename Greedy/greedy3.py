#a,b는 둘다 리스트, a[i]가 b[i]의 배수가 되도록하는 버튼 누르는 횟수의 최솟값을 구하여라
#a[i]를 누르면 a[i]부터 a[n-1]까지의 값이 +1씩 된다

def solution(a,b):
    n = len(a)
    sum = 0
    for i in range(n-1,-1,-1):
        a[i] +=sum
        if a[i]% b[i] != 0:
            d = b[i] - (a[i] % b[i])
            sum+=d
    return sum
print(solution([1,1,3],[4,5,6]))