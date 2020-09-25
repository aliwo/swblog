def solution(numbers):
    answer = set()

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    answer = list(answer)
    answer.sort()

    return answer

print(solution([2,1,3,4,1])) # [2,3,4,5,6,7]
print(solution([5,0,2,7])) # [2,5,7,9,12]