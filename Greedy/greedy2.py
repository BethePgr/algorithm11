#회의시간이 주어진 리스트에서 최대한 많은 회의를 담을 수 있는 방법

def solution(list):
    list.sort(key = lambda x : (x[1],x[0]))
    result = 1
    endtime = list[0][1]
    for i in range(len(list)):
        if list[i][0] > endtime:
            endtime = list[i][1]
            result +=1
    return result

print(solution([[9,16],[10,12],[11.5,15.1],[13,18.9],[15,18],[19,22]]))