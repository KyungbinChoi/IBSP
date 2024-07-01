import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

mu, sigma, n = 70, 8, 5

# code here
# 평균이 mu이고 표준편차가 sigma이며 크기가 5인 정규분포를 50000회 샘플링하자
norms = np.random.normal(mu, sigma, (50000, n))

# 크기가 5인 각각의 샘플에서, 각각의 평균을 구한 뒤 모평균을 빼고 각 샘플의 표준 편차/루트n으로 나눠주자.
sample_means = np.mean(norms, axis=1)
sample_stds = np.std(norms, axis=1, ddof=1)
norms_normalized = (sample_means - mu) / (sample_stds / np.sqrt(n))

# 위의 표준화된 표본평균들 중 -3~3사이인 값들만 남기자
norms_normalized = norms_normalized[(norms_normalized>=-3)&(norms_normalized<=3)]

xs = np.linspace(norm.ppf(0.001), norm.ppf(0.999), 1000)
ps_norm = norm.pdf(xs)# xs에 있는 각 x 값에 대한 정규분포의 pdf를 뽑자
ps_t = t.pdf(xs, df= n-1) # xs에 있는 각 x 값에 대한 자유도가 n-1인 t 분포의 pdf를 뽑자

plt.hist(norms_normalized, bins=50, density=True, color='skyblue', alpha=0.8)
plt.plot(xs, ps_norm, color='red')
plt.plot(xs, ps_t, color='green')
plt.xlim(-3, 3)
plt.legend(['normal', 't'])
plt.show()
