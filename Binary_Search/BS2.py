#LOWER BOUND 구현해보기
def solution(a,b): #a는 리스트, b는 찾고자 하는 값, 이 함수는 b이상의 값이 시작되는 인덱스를 찾는 함수이다.
    left = 0
    right = len(a)
    while right -1 > left:
        mid = (right + left) // 2
        if a[mid] >= b:
            right = mid
        elif a[mid] < b:
            left = mid

    return right

print(solution([1,2,11,14,15,196],196))