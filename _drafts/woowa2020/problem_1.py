
grades_dict = {
    'A+': 10,
    'A0': 9,
    'B+': 8,
    'B0': 7,
    'C+': 6,
    'C0': 5,
    'D+': 4,
    'D0': 3,
    'F': 0,
}

def solution(grades, weights, threshold):
    return sum([grades_dict[grade] * weight for grade, weight in zip(grades, weights)]) - threshold

print((solution(["A+","D+","F","C0"], [2,5,10,3], 50)))
print((solution(["B+","A0","C+"], [6,7,8], 200)))