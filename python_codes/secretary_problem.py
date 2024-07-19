"""
비서 1명을 뽑는 공고에 100명의 사람이 지원했습니다. 당신은 1명씩 면접을 진행하며, 합불여부를 바로 현장에서 통보해야 합니다.
한 번 불합격시킨 면접자는 다시 번복할 수 없고 합격자가 나오면 이후의 모든 면접은 취소됩니다. 
당신의 목표는 100명 중 가장 뛰어난 지원자를 뽑는 것입니다. 
당신은 k%의 지원자를 본 뒤 그 중 가장 뛰어난 지원자보다 뛰어난 지원자를 나머지 (100-k)%의 지원자 중에서 만나면 뽑기로 결정했습니다. 최적의 k를 시뮬레이션을 통해 구해보세요.
"""

import random

def interview(k):
    scores = list(range(1, 101))
    # code here
    
    random.shuffle(scores) # scores를 shuffle

    explore = scores[:k]# scores중 앞의 k개
    max_explore = max(explore)

    max_found = False
    for idx, score in enumerate(scores[k:]):
        if score > max_explore:
            if score == 100:
                return True
            else:
                return False

    return False

def interview_iterator(n, k):
    interviewed = [interview(k) for i in range(n)]
    found_count = sum([i for i in interviewed])
    print(f"{n}회 중 성공 횟수: {found_count}({100 * found_count / n}%)")

if __name__ == "__main__":
    interview_iterator(10000, 50)

    interview_iterator(10000, 75)

    interview_iterator(10000, 25)

    interview_iterator(10000, 37)

"""
10000회 중 성공 횟수: 3564(35.64%)

10000회 중 성공 횟수: 2098(20.98%)

10000회 중 성공 횟수: 3506(35.06%)

10000회 중 성공 횟수: 3776(37.76%)
"""