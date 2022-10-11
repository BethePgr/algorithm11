#동전 내기 문제
def solution(price):
    list = [500,100,50,10]
    answer = []
    for i in range(len(list)):
        a = price // list[i]
        price = price % list[i]
        answer.append(a)
    return answer

print(solution(2430))