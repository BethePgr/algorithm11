#Frog problem(5장)
"""
1번지 가는 방법:
0에서 1

2번지 가는 방법:
1.0 번지에서 2번지
2.1 번지에서 2번지

3번지 가는 방법:
1.1 번지에서 3번지
2.2 번지에서 3번지
"""

def solution(list):
    #list는 개구리가 가는 기둥의 높이가 담겨져 있는 리스트
    dp_list=[]
    dp_list.append(0)
    for i in range(1,len(list)):
        if i == 1:
            dp_list.append(abs(list[1]-list[0]))
        else:
            dp_list.append(min(dp_list[i-2]+abs(list[i]-list[i-2]),dp_list[i-1]+abs(list[i]-list[i-1])))
    return dp_list

print(solution([2,9,4,5,1,6,10]))