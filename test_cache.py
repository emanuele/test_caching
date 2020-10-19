from joblib import Memory

cache_dir = '/tmp/bbb'
memory = Memory(cache_dir, verbose=False)

@memory.cache
def f(x):
    print('executing f(%s)' % x)
    return x

