import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

norms = [np.random.normal(0,1,10) for _ in range(100000)]
# 정규분포에서 난수 추출된 리스트들의 각각의 제곱합을 구하시오
ss = [np.sum(np.square(norm)) for norm in norms]
print(ss[:10])
xs = np.arange(0, np.max(ss), 0.01)
# 자유도가 10인 카이스퀘어 분포로부터 각 x에 해당하는 확률 값을 구하시오
ps = chi2.pdf(xs,df=10)

plt.hist(ss, bins = 50, density=True)
plt.plot(xs, ps, color='red')
plt.show()
