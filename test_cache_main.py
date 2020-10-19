import numpy as np
from joblib import Parallel, delayed
from test_cache import f

if __name__=='__main__':

    np.random.seed(0)
    xs = [np.random.uniform(size=(1000,1000)) for i in range(20)]
    result = [Parallel(n_jobs=-1, require='sharedmem', verbose=50)(delayed(f)(x) for x in xs)]
