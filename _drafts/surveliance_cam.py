def solution(routes):
    routes.sort()  # 오름 차순 정렬. 진입 지점이 같으면 먼저 나가는 것 부터.
    answer = 0

    i = 0
    while i < len(routes):
        temp_q = [routes[i]]
        temp_out = routes[i][1]  # 겹치는 차량들 중 가장 빨리 나가는 차량
        i += 1
        while i < len(routes):
            if temp_out >= routes[i][0]:
                temp_q.append(routes[i])
                temp_out = routes[i][1] if temp_out > routes[i][1] else temp_out
                i += 1
            else:
                answer += 1  # temp_out 에 카메라를 꽂으면 된다.
                break
        else:
            answer += 1
            break

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.7MB)
테스트 2 〉	통과 (0.06ms, 10.8MB)
테스트 3 〉	통과 (0.07ms, 10.7MB)
테스트 4 〉	통과 (0.07ms, 10.7MB)
테스트 5 〉	통과 (0.07ms, 10.9MB)
효율성  테스트
테스트 1 〉	통과 (1.17ms, 11.7MB)
테스트 2 〉	통과 (0.79ms, 11.2MB)
테스트 3 〉	통과 (2.87ms, 15.9MB)
테스트 4 〉	통과 (0.11ms, 10.9MB)
테스트 5 〉	통과 (3.31ms, 17.3MB)
'''

def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
