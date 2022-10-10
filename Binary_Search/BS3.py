#나이 맞추기 게임 나이는 20세 이상 36세 미만으로 설정, 4번 미만으로 정답을 맞출수있나?
def solution(a,b,c): #a세 이상 b세 미만으로 설정 c는 찾으려는 나이
    answer=1
    left = a
    right = b
    while right -1 > left:
        mid = (left + right) // 2
        if mid == c:
            return answer
        elif mid > c:
            right = mid
            answer+=1
        elif mid < c:
            left = mid
            answer+=1
    return answer

print(solution(20,36,31))
