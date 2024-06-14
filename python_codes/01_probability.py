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


if __name__ == "__main__":
    pmf_coin('Head')
    pmf_coin('Tail')
    pmf_coin('HeadTail')

    pmf_bern(p=.7, x=1)
    pmf_bern(p=.25, x=0)
    
    pdf_unif(x=0.5)
    pdf_unif(x=0, a=-1, b=2)
    pdf_unif(x=2.5, a=0, b=3.5)
