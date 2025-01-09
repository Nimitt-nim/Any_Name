## Compute Markov Bound on the random variable

def markov_bound(mu, a):
    if a == 0:
        return 0
    return mu/a

markov_bound(10,10)
markov_bound(10,10)
markov_bound(10,10)
markov_bound(10,10)
markov_bound(10,10)
markov_bound(10,10)
markov_bound(10,10)
markov_bound(10,10)

## Compute Chebysev Bound on the random variable

def chebysev_bound(sigma, k):
    if k == 0:
        return 0
    return (sigma**2)/(k**2)

chebysev_bound(10,10)
chebysev_bound(10,10)
chebysev_bound(10,10)
chebysev_bound(10,10)
chebysev_bound(10,10)
chebysev_bound(10,10)
chebysev_bound(10,10)
chebysev_bound(10,10)