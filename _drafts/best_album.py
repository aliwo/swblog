from collections import defaultdict


class Genre:

    def __init__(self):
        self.total = 0
        self.tracks = []

    def insert(self, index, play):
        self.total += play
        self.tracks.append((play, index))


def solution(genres, plays):
    answer = []
    cache = defaultdict(lambda : Genre())
    i = 0
    while i < len(genres):
        cache[genres[i]].insert(i, plays[i])
        i += 1

    for genre in sorted(cache.values(), key=lambda x: x.total, reverse=True):
        for elem in sorted(genre.tracks, key=lambda y: (-y[0], y[1]))[:2]:
            answer.append(elem[1])

    return answer


# 내 답 보다 미세하게 빠르다... 왜?
# 정렬 시키면서 집어넣는 것 보다 나중에 정렬하는게 빠르다는건가?

# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)} # 여기서 모든 genre 를 n 번 회전하고
#     for e in zip(genres, plays, range(len(plays))): # 다시 n 번 회전 한다. 따라서 2n
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True) # lambda y 에 의해 또 회전, 3n
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)] # 4n
#         answer += temp[:min(len(temp),2)]
#     return answer


assert solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4,1,3,0]
assert solution(["classic", "pop", "classic", "classic", "pop", 'kimchi'], [500, 600, 150, 800, 2500, 100]) == [4,1,3,0,5]
