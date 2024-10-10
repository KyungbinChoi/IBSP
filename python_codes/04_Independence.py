# 독립성 가정을 충족하는 통계적 검정
"""
T-test 에서 필요한 가정은 독립성과 등분산성
자기상관성을 확인하기 위한 검정으로 Durbin-watson test 를 이용 (연속해서 평균보다 높은 값이 나오거나 낮은 값이 나오는 경우가 우연으로 보기 힘들 정도로 많은지를 판단)
    - 검정 통계량은 2를 기준으로 2 주변 값이면 자기상관성이 존재하지 않음. 2보다 크면 양의 자기상관성, 작으면 음의 자기상관성을 가진다 판단
    
"""

import time

import numpy as np
from statsmodels.stats.stattools import durbin_watson
import matplotlib.pyplot as plt
np.random.seed(123)
n1 = n2 = 200

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

dw_stats_assign = durbin_watson(append_assign_time)
dw_stats_direct = durbin_watson(append_direct_time)

print(f"DW test statistic without dot: {dw_stats_direct:.4f}")
print(f"DW test statistic with dot: {dw_stats_assign:.4f}")

plt.figure(figsize=(15,4))
plt.subplot(1,2,1)
plt.plot(append_direct_time)
plt.title('without dot')
plt.xlabel('index')
plt.ylabel('elapsed time')

plt.subplot(1,2,2)
plt.plot(append_assign_time)
plt.title('with dot')
plt.xlabel('index')
plt.ylabel('elapsed time')
plt.show()
