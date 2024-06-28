from scipy.stats import binom
def binom_exp(n, p):
    '''
    이항 분포에 대해, 주어진 모수를 가지고 모든 가능한 경우의 수의 확률을 구하고, 
    이를 토대로 평균과 분산이라는 기댓값을 구해보자
    '''
    xs = n
    probs = p
    mean = xs*probs
    var = xs*probs*(1-probs)

    print(f"Mean of Binom({n}, {p}): {mean:.2f}")
    print(f"Variance of Binom({n}, {p}): {var:.2f}")


if __name__ == "__main__":
    binom_exp(10, .2)

    binom_exp(3, .9)

    binom_exp(200, .05)

    binom_exp(200, .5)
