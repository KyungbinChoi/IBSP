# IQ가 주어진 평균과 표준 편차를 갖는 정규 분포를 따른다고 할 때, 상위 q의 해당하는 IQ를 구하기

from scipy.stats import norm

def iq_percentile(q, mu, std):
    iq = (norm.ppf(1-q,)*std) + mu# code here
    print(f"IQ가 평균 {mu}, 표준편차 {std}인 정규 분포를 따를 때")
    print(f"상위 {q*100:.2f}%의 IQ: {iq:.2f}")


if __name__ == "__main__":
    iq_percentile(0.01, 100, 24)

    iq_percentile(0.10, 100, 24)

    iq_percentile(0.025, 100, 16)

    iq_percentile(0.5, 100, 16)
