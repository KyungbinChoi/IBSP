import time

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

append_direct_time = []
for _ in range(1000):
    start = time.time()
    num_list = []
    for i in range(10000):
        num_list.append(i)
    end = time.time()
    append_direct_time.append(end-start)

append_assign_time = []
for _ in range(1000):
    start = time.time()
    num_list = []
    list_append = num_list.append
    for i in range(10000):
        list_append(i)
    end = time.time()
    append_assign_time.append(end-start)

print(f"append_direct_time의 평균: {np.mean(append_direct_time):.6f}")
print(f"append_direct_time의 중간값: {np.median(append_direct_time):.6f}")
print(f"append_direct_time의 표준편차: {np.var(append_direct_time):.6f}")
print(f"append_direct_time의 최솟값: {np.min(append_direct_time):.6f}")
print(f"append_direct_time의 최댓값: {np.max(append_direct_time):.6f}")

print(f"append_assign_time의 평균: {np.mean(append_assign_time):.6f}")
print(f"append_assign_time의 중간값: {np.median(append_assign_time):.6f}")
print(f"append_assign_time의 표준편차: {np.var(append_assign_time):.6f}")
print(f"append_assign_time의 최솟값: {np.min(append_assign_time):.6f}")
print(f"append_assign_time의 최댓값: {np.max(append_assign_time):.6f}")

x_max = np.where(max(append_direct_time) > max(append_assign_time), max(append_direct_time), max(append_assign_time))
x_min = np.where(min(append_direct_time) < min(append_assign_time), min(append_direct_time), min(append_assign_time))
bins = np.linspace(x_min, x_max , 20)

plt.hist(append_direct_time, color='skyblue', alpha=0.5, bins=bins)
plt.hist(append_assign_time, color='pink', alpha=0.5, bins=bins)
plt.legend(['append_direct_time', 'append_assign_time'])
plt.show()

t_statistic, p_value = stats.ttest_ind(append_direct_time, append_assign_time)
print(f"t통계량: {t_statistic:.2f}")
print(f"p값: {p_value:.4f}")