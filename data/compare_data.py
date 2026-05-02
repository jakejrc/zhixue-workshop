# -*- coding: utf-8 -*-
"""算法实战对比器 - 数据集与算法定义"""

COMPARE_DATASETS = {
    'iris': {
        'name': 'Iris 鸢尾花',
        'description': '150样本，4特征，3类',
        'samples': 150,
        'features': 4,
        'classes': 3,
        'task': 'classification',
        'load_code': 'from sklearn.datasets import load_iris\nX, y = load_iris(return_X_y=True)',
    },
    'wine': {
        'name': 'Wine 葡萄酒',
        'description': '178样本，13特征，3类',
        'samples': 178,
        'features': 13,
        'classes': 3,
        'task': 'classification',
        'load_code': 'from sklearn.datasets import load_wine\nX, y = load_wine(return_X_y=True)',
    },
    'moons': {
        'name': '双月形(合成)',
        'description': '200样本，2特征，2类，非线性',
        'samples': 200,
        'features': 2,
        'classes': 2,
        'task': 'classification',
        'load_code': 'from sklearn.datasets import make_moons\nX, y = make_moons(n_samples=200, noise=0.3, random_state=42)',
    },
    'circles': {
        'name': '同心圆(合成)',
        'description': '200样本，2特征，2类，非线性',
        'samples': 200,
        'features': 2,
        'classes': 2,
        'task': 'classification',
        'load_code': 'from sklearn.datasets import make_circles\nX, y = make_circles(n_samples=200, noise=0.2, factor=0.5, random_state=42)',
    },
    'blobs': {
        'name': '聚类团(合成)',
        'description': '300样本，2特征，4类，线性可分',
        'samples': 300,
        'features': 2,
        'classes': 4,
        'task': 'classification',
        'load_code': 'from sklearn.datasets import make_blobs\nX, y = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)',
    },
}

COMPARE_ALGORITHMS = {
    'knn': {
        'name': 'KNN',
        'icon': 'bi-people',
        'desc': '基于最近邻投票，简单直观',
        'params': {'n_neighbors': 5},
    },
    'dt': {
        'name': '决策树',
        'icon': 'bi-diagram-3',
        'desc': '基于特征分裂的树形结构',
        'params': {'max_depth': 5, 'random_state': 42},
    },
    'svm': {
        'name': 'SVM',
        'icon': 'bi-arrows-angle',
        'desc': '寻找最大间隔超平面',
        'params': {'kernel': 'rbf', 'random_state': 42},
    },
    'lr': {
        'name': '逻辑回归',
        'icon': 'bi-graph-up',
        'desc': '线性模型+sigmoid激活',
        'params': {'max_iter': 200, 'random_state': 42},
    },
    'nb': {
        'name': '朴素贝叶斯',
        'icon': 'bi-bar-chart',
        'desc': '基于贝叶斯定理的概率分类',
        'params': {},
    },
    'mlp': {
        'name': '神经网络(MLP)',
        'icon': 'bi-diagram-2',
        'desc': '多层感知器，非线性拟合能力强',
        'params': {'hidden_layer_sizes': (50,), 'max_iter': 500, 'random_state': 42},
    },
}
