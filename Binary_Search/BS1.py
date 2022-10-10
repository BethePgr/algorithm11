#가장 기본적인 이진 탐색법 코드
def solution(a,b): #a는 리스트 b는 찾으려고하는 값
    left = 0
    right = len(a) - 1
    while right >= left:
        mid = (left + right)//2
        if a[mid] == b:
            return mid
        elif b > a[mid]:
            left = mid + 1
        elif b < a[mid]:
            right = mid - 1
    return False

print(solution([1,2,3,4,10,15,46,67,88],15))
