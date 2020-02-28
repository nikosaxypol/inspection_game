from numpy import arange

last_x = 'N/A'
last_y = 'N/A'

def x(a, b, c, d):
    if a > c and b > d:
        return 1
    if c > a and d > b:
        return 0
    x = (d-c)/(a-b-c+d)
    return x

def y(a, b, c, d):
    if b > a and d > c:
        return 1
    if a > b and c > d:
        return 0
    y = (d-b)/(a-b-c+d)
    return y

def value(x, a, c):
    return x*a + c*(1-x)

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

"""
computes n per m
If n > m, computes m per n
"""
def combination(n, m):
    if m > n:
        tmp = n
        n = m
        m = tmp
    if m == 0:
        return 1

    return factorial(n)/(factorial(n-m)*factorial(m))

def summary(n, k, q):
    s = 0
    for j in range(0, k):
        s += (k-j)*combination(n-k-1+j, j)*(q**j)
    return s

def o(n, k, q):
    return k-(1-q)**(n-k+1)*summary(n,k, q)

def G(n, k, l, q):

    global last_x
    global last_y

    # TODO: remove asserts
    if not (0<=k and k<=n):
        return 0
    if not (0<=l and l<=n):
        return 0
    if not (type(n) == int):
        return 0
    if not (type(k) == int):
        return 0
    if not (type(l) == int):
        return 0

    if k == 0:
        v = 0
    elif l == 0:
        v = 0;
    elif n == k:
        v = l*q
    elif n == l:
        v = o(n,k,q)
    else:
        a = G(n-1, k-1, l-1, q) + 1
        b = G(n-1, k-1, l  , q)
        c = G(n-1, k  , l-1, q)
        d = G(n-1, k  , l  , q)

        _x = x(a, b, c, d)
        _y = y(a, b, c, d)

        last_x = _x
        last_y = _y

        v = value(_x, a, c)

    return v

min_q = 0.5
max_q = 0.5
step_q = 0.1

min_n = 16
max_n = 16

min_k = 15
max_k = 15

min_l = 16
max_l = 16

for n in range(min_n, max_n+1):
    for k in range(min_k, max_k+1):
        for l in range(min_l, max_l+1):
            for q in range(int(min_q*10), int(max_q*10) + int(step_q*10), int(step_q*10)):
                _q = q/10
                # print(n, k, l, _q)
                g = G(n, k, l, _q)
                print(g, '\t', last_x, '\t', last_y)
