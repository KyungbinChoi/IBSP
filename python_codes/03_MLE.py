import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

np.random.seed(85)
lamb = 3
samples = np.random.poisson(lamb, 30)

# 후보 람다 값 설정
lamb_cand = np.arange(1, 8)
likelihoods = []

# 우도 계산 함수 정의
def calculate_likelihood(lamb, samples):
    likelihood = np.prod([poisson.pmf(sample, lamb) for sample in samples])
    return likelihood

# 각 후보 람다 값에 대해 우도 계산
for lamb in lamb_cand:
    likelihood = calculate_likelihood(lamb, samples)
    likelihoods.append(likelihood)

# 우도 시각화
plt.plot(lamb_cand, likelihoods, marker='o')
plt.xlabel('Lambda (λ)')
plt.ylabel('Likelihood')
plt.title('Likelihood of λ for Poisson-distributed data')
plt.grid(True)
plt.show()
