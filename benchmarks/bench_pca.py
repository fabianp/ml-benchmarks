"""PCA benchmarks"""

import numpy as np
from datetime import datetime

#
#       .. Load dataset ..
#
from misc import load_data, bench
print 'Loading data ...'
X, y, T = load_data()
print 'Done, %s samples with %s features loaded into ' \
      'memory' % X.shape
n_components = 9



def bench_skl():
#
#       .. scikits.learn ..
#
    from scikits.learn import pca as skl_pca
    start = datetime.now()
    clf = skl_pca.RandomizedPCA(n_components=n_components)
    clf.fit(X)
    return datetime.now() - start


def bench_pybrain():
#
#       .. pybrain ..
#
    from pybrain.auxiliary import pca as pybrain_pca
    start = datetime.now()
    pybrain_pca.pca(X, n_components)
    return datetime.now() - start


def bench_mdp():
#
#       .. MDP ..
#
    from mdp.nodes import PCANode
    start = datetime.now()
    mdp_clf = PCANode(output_dim=n_components)
    mdp_clf.train(X)
    return datetime.now() - start


def bench_pymvpa():
#
#       .. PyMVPA ..
#
    from mvpa.mappers.mdp_adaptor import PCAMapper as MVPA_PCA
    from mvpa.datasets import dataset_wizard
    start = datetime.now()
    clf = MVPA_PCA(output_dim=n_components)
    data = dataset_wizard(samples=X)
    clf.train(data)
    return datetime.now() - start

def bench_milk():
#
#       .. milk ..
#
    from milk.unsupervised import pca as milk_pca
    start = datetime.now()
    _ = milk_pca(X)
    return datetime.now() - start


if __name__ == '__main__':

    # don't bother me with warnings
    import warnings; warnings.simplefilter('ignore')
    np.seterr(all='ignore')

    print __doc__ + '\n'

    res_mdp = bench(bench_mdp)
    print 'MDP: mean %s, std %s' % (
        np.mean(res_mdp), np.std(res_mdp))

    res_skl = bench(bench_skl)
    print 'scikits.learn: mean %s, std %s' % (
        np.mean(res_skl), np.std(res_skl))

    res_pybrain = bench(bench_pybrain)
    print 'Pybrain: mean %s, std %s' % (
        np.mean(res_pybrain), np.std(res_pybrain))

    res_milk = bench(bench_milk)
    print 'milk: mean %s, std %s' % (
        np.mean(res_milk), np.std(res_milk))

    res_pymvpa = bench(bench_pymvpa)
    print 'PyMVPA: mean %s, std %s' % (
        np.mean(res_pymvpa), np.std(res_pymvpa))
