# n 의 크기에 따라 신뢰 구간의 길이가 달라지는 것을 확인하는 시뮬레이션
import time
import numpy as np
from scipy.stats import t

def t_test_calculator(n, alpha):
    normal_sample = np.random.normal(0, 1, n)

    X_bar = np.mean(normal_sample)
    df = n-1 # degree of freedomm
    std = np.std(normal_sample , ddof= 1)
    se = std / np.sqrt(len(normal_sample))
    T = t.ppf(1-alpha/2, df) 
    p_value = 2 * (1-t.cdf(abs(X_bar / se), df))# 양측 검정
    # 신뢰 구간 (Confidence Interval)
    ci_lower = X_bar - T * se
    ci_upper = X_bar + T * se
    ci = (ci_lower, ci_upper)

    return (p_value, *ci)

np.random.seed(805)

alpha = 0.05
ns = np.arange(10, 50, 3)
p_values = []
ci_lowers = []
ci_uppers = []

for n in ns:
    p_value, ci_lower, ci_upper = t_test_calculator(n, alpha)
    print(f"n = {n}, p-values: {p_value:.4f}, CI: ({ci_lower:.2f}, {ci_upper:.2f})")
    p_values.append(p_value)
    ci_lowers.append(ci_lower)
    ci_uppers.append(ci_upper)
