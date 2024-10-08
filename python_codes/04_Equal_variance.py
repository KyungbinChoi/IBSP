import time

import numpy as np
from scipy.stats import t

n1 = n2 = 1000

append_direct_time = []
for _ in range(n2):
    start = time.time()
    num_list = []
    for i in range(10000):
        num_list.append(i)
    end = time.time()
    append_direct_time.append(end-start)

append_assign_time = []
for _ in range(n1):
    start = time.time()
    num_list = []
    list_append = num_list.append
    for i in range(10000):
        list_append(i)
    end = time.time()
    append_assign_time.append(end-start)

# 두 집단의 평균, 분산 계산
X_bar1 = np.mean(append_direct_time)
X_bar2 = np.mean(append_assign_time)
sigma1 = np.var(append_direct_time, ddof=1)  # 비편향 분산
sigma2 = np.var(append_assign_time, ddof=1)  # 비편향 분산

# Welch's t-test를 위한 t-statistic 계산
s_delta = np.sqrt(sigma1/n1 + sigma2/n2)
T = (X_bar1 - X_bar2) / s_delta

# 자유도 계산 (Welch-Satterthwaite equation)
df = (sigma1/n1 + sigma2/n2)**2 / ((sigma1**2 / (n1**2 * (n1 - 1))) + (sigma2**2 / (n2**2 * (n2 - 1))))

# p-value 계산 (양측 검정)
p_value = 2 * (1 - t.cdf(np.abs(T), df))

# 결과 출력
print(f"P-value: {p_value:.4f}")