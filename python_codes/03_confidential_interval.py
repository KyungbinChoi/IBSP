#정규 분포로부터 난수추출한 데이터에 대해, 추정하고자 하는 모평균의 95% 신뢰 구간을 측정하는 함수를 만들고 표본 크기에 따른 신뢰 구간의 길이를 시각화하는 코드

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def CI_calculator(mu, sigma, alpha, n, ci_print=False):
    samples = np.random.normal(loc=mu, scale=sigma, size=n)
    x_bar = np.mean(samples)# code here
    SE = sigma / np.sqrt(n)  # 표준 오차 계산
    z_value = norm.ppf(1 - alpha / 2)  # 신뢰도 수준에 따른 Z값 계산

    error_bound = z_value * SE  # 신뢰 구간의 한계 오차 계산
    upper_bound = x_bar + error_bound  # 신뢰 구간 상한
    lower_bound = x_bar - error_bound  # 신뢰 구간 하한
    CI_length = upper_bound - lower_bound  # 신뢰 구간의 길이

    if ci_print:
        print(f"평균 {mu}, 표준 편차 {sigma}, 신뢰 수준 {1-alpha}, 표본 개수 {n}일 때")
        print(f"모평균의 점추정값: {x_bar:.2f}, 신뢰구간: ({lower_bound:.2f}, {upper_bound:.2f})")
    else:
        return CI_length

def CI_length_plotter(ns):
    CI_lengths = []
    for n in ns:
        CI_lengths.append(CI_calculator(10, 5, 0.05, n))

    plt.plot(ns, CI_lengths)
    plt.xlabel('The number of samples')
    plt.ylabel('CI length')
    plt.show()


CI_calculator(10, 5, 0.05, 100, True)

CI_calculator(10, 5, 0.01, 100, True)

CI_calculator(10, 5, 0.05, 1000, True)

ns = (10, 20, 50, 100, 200, 500, 1000)
CI_length_plotter(ns)