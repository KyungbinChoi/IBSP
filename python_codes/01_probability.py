from scipy.stats import norm,binom,poisson
import matplotlib.pyplot as plt

def pmf_coin(outcome):
    '''
    본 함수는 동전을 던졌을 때 나오는 결과(Head 혹은 Tail)를 입력값으로 받는다.
    입력값 outcome이 Head와 Tail 둘 중 하나일 때는 0.5, 그 외에는 0이 확률이 된다.
    확률 변수의 형식으로, 주어진 outcome에 대한 확률을 출력한다.
    '''
    if outcome in ("Head", "Tail"):
        p = 0.5

    else:
        p = 0

    print(f"P(X = x) = {p:.2f}")

def pmf_bern(p, x):
    '''
    주어진 p와 x에 관한 베르누이 분포의 확률 값을 반환한다.
    x는 0과 1만이 가능하다.
    '''
    if x == 1: 
        prob = p
    else:
        prob = 1-p
    print(f"P(X={x}; p={p}) = {prob:.2f}")
    return prob

def pdf_unif(x, a=0, b=1):
    '''
    주어진 a, b, x에 관한 균등 분포의 확률 값을 출력한다.
    '''
    if x >= a and x <= b:
        prob = (x-a)/(b-a)
    else:
        prob = 0
    print("P(X=%s; a=%s, b=%s) = %.2f"%(x, a, b, prob))

def pdf_norm(x, mu=0, sigma=1):
    '''
    주어진 x, mu, sigma에 관한 정규 분포의 확률 값을 출력한다.
    '''
    prob = norm.pdf(x, mu,sigma)
    print(f"P(X={x}; mu={mu}, sigma={sigma}) = {prob:.2f}")

def pdf_binom(x, n, p):
    '''
    주어진 x, n, p 관한 이항 분포의 확률 값을 출력한다.
    '''
    prob = binom.pmf(x,n,p)
    print(f"P(X={x}; n={n}, p={p}) = {prob:.2f}")

def pmf_poisson_graphing(lamb):
    '''
    주어진 lambda에 대한 확률값을 시각화한다.
    x의 범위는 [0, 3*lambda]이다.
    '''
    xs = list(range(3*lamb))
    ps = [poisson.pmf(x, lamb) for x in xs]

    fig, ax = plt.subplots()
    ax.plot(
        # code here
        xs, ps,
        marker='o'
    )

    plt.show()

if __name__ == "__main__":
    # 확률
    pmf_coin('Head')
    pmf_coin('Tail')
    pmf_coin('HeadTail')

    #베르누이 분포 
    pmf_bern(p=.7, x=1)
    pmf_bern(p=.25, x=0)

    # pdf
    pdf_unif(x=0.5)
    pdf_unif(x=0, a=-1, b=2)
    pdf_unif(x=2.5, a=0, b=3.5)

    # 정규 분포
    pdf_norm(0)
    pdf_norm(1.96, 0, 1)
    pdf_norm(-1, 2, 10)

    # 이항분포
    pdf_binom(x=3, n=10, p=0.3)
    pdf_binom(x=7, n=10, p=0.7)
    pdf_binom(x=50, n=100, p=0.1)

    pmf_poisson_graphing(3)
    pmf_poisson_graphing(7)
