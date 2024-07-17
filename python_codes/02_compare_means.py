from collections import Counter, OrderedDict
from scipy.stats import norm, binom
import numpy as np

def binom_counter(size):
    samples = binom.rvs(5, 0.3, size=size) # code here n=5이고 p=0.3인 이항 분포에서 size만큼의 표본을 추출

    for value, count in sorted(Counter(samples).items()):
        print(f"값이 {value}인 표본의 수: {count}({100*count/size:.2f}%)")

def compare_sample_prob(lower_bound, upper_bound):
    norm_samples = norm.rvs(0, 1, 100000)

    # lower_bound와 upper_bound 사이의 값을 갖는 샘플들
    target_samples = norm_samples[(norm_samples >= lower_bound) & (norm_samples <= upper_bound)]
    
    # 해당 샘플들의 비율
    target_sample_prop = len(target_samples) / len(norm_samples)
    
    # 표본 정규 분포가 lower_bound와 upper_bound 사이의 값을 가질 확률
    target_prob = norm.cdf(upper_bound, 0, 1) - norm.cdf(lower_bound, 0, 1)

    print(f"표본에서 타겟 샘플의 비율: {target_sample_prop:.4f}")
    print(f"확률 분포에서 타겟 샘플의 확률: {target_prob:.4f}")

if __name__ == "__main__":
    binom_counter(10000)

    compare_sample_prob(0, 1)

    compare_sample_prob(0, 2)

    compare_sample_prob(0, 3)

    compare_sample_prob(-1, 0)

    compare_sample_prob(-np.inf, 0)

    compare_sample_prob(-1, 1)
