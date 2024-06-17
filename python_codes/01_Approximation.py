from scipy.stats import binom, poisson, norm
import matplotlib.pyplot as plt

def poisson_binom_plot(n, p):
    lamb = n*p# code here
    mu = n*p
    std = n*p*(1-p)

    x_min = int(-n*0.2)
    x_max = int(n*1.2)

    probs_binom = [binom.pmf(i,n,p) for i in range(x_min, x_max+1)]
    probs_poisson = [poisson.pmf(x, lamb) for x in range(x_min,x_max+1)] # code here
    probs_norm = [norm.pdf(x, mu, std) for x in range(x_min, x_max+1)] # code here

    plt.plot(range(x_min, x_max+1), probs_binom, alpha=0.5)
    plt.plot(range(x_min, x_max+1), probs_poisson, alpha=0.5)
    plt.plot(range(x_min, x_max+1), probs_norm, alpha=0.5)
    plt.legend(['binom', 'poisson', 'norm'])
    plt.title(f'N={n}, p={p}')
    plt.show()

if __name__ == "__main__":
    poisson_binom_plot(5, 0.9)
    # poisson_binom_plot(20, 0.4)
    # poisson_binom_plot(20, 0.9)
    # poisson_binom_plot(40, 0.9)
    # poisson_binom_plot(100, 0.0001)