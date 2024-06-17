from scipy.stats import binom, poisson, norm
import matplotlib.pyplot as plt

def poisson_binom_plot(n, p):
    # lamb = # code here
    # mu = # code here
    # std = # code here

    x_min = int(-n*0.2)
    x_max = int(n*1.2)

    probs_binom = [binom.pmf(i,n,p) for i in range(x_min, x_max+1)]
    # probs_poisson = # code here
    # probs_norm = # code here

    plt.plot(range(x_min, x_max+1), probs_binom, alpha=0.5)
    plt.plot(range(x_min, x_max+1), probs_poisson, alpha=0.5)
    plt.plot(range(x_min, x_max+1), probs_norm, alpha=0.5)
    plt.legend(['binom', 'poisson', 'norm'])
    plt.title(f'N={n}, p={p}')
    plt.show()
