# -*- coding: utf-8 -*-
"""算法实战对比器蓝图 - 同一数据集跑不同算法，对比结果"""
import time, io, base64, json
from flask import Blueprint, render_template, request, jsonify
from data.compare_data import COMPARE_DATASETS, COMPARE_ALGORITHMS

compare_tool_bp = Blueprint('compare_tool', __name__, url_prefix='/compare-tool')

def _load_dataset(dataset_key):
    """加载数据集，返回(X, y, X_2d, feature_names)"""
    from sklearn.datasets import load_iris, load_wine, make_moons, make_circles, make_blobs
    from sklearn.decomposition import PCA
    import numpy as np

    if dataset_key == 'iris':
        data = load_iris()
        X, y = data.data, data.target
        names = data.feature_names
    elif dataset_key == 'wine':
        data = load_wine()
        X, y = data.data, data.target
        names = data.feature_names
    elif dataset_key == 'moons':
        X, y = make_moons(n_samples=200, noise=0.3, random_state=42)
        names = ['特征1', '特征2']
    elif dataset_key == 'circles':
        X, y = make_circles(n_samples=200, noise=0.2, factor=0.5, random_state=42)
        names = ['特征1', '特征2']
    elif dataset_key == 'blobs':
        X, y = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)
        names = ['特征1', '特征2']
    else:
        return None, None, None, None

    # 降到2维用于可视化
    if X.shape[1] > 2:
        pca = PCA(n_components=2, random_state=42)
        X_2d = pca.fit_transform(X)
    else:
        X_2d = X

    return X, y, X_2d, names

def _get_classifier(algo_key, params):
    """获取分类器实例"""
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from sklearn.neural_network import MLPClassifier

    classifiers = {
        'knn': KNeighborsClassifier,
        'dt': DecisionTreeClassifier,
        'svm': SVC,
        'lr': LogisticRegression,
        'nb': GaussianNB,
        'mlp': MLPClassifier,
    }
    cls = classifiers.get(algo_key)
    if cls is None:
        return None
    return cls(**params)

def _plot_decision_boundary(clf, X_2d, y, title):
    """绘制决策边界，返回base64图片"""
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

    h = 0.02
    x_min, x_max = X_2d[:, 0].min() - 0.5, X_2d[:, 0].max() + 0.5
    y_min, y_max = X_2d[:, 1].min() - 0.5, X_2d[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    fig, ax = plt.subplots(1, 1, figsize=(5, 4))
    cmap_bg = ListedColormap(['#FFEEEE', '#EEFFEE', '#EEEEFF', '#FFFFEE', '#FFEEFF', '#EEFFFF'])
    cmap_pts = ListedColormap(['#e74a3b', '#1cc88a', '#4e73df', '#f6c23e', '#6f42c1', '#17a2b8'])

    ax.contourf(xx, yy, Z, alpha=0.3, cmap=cmap_bg)
    scatter = ax.scatter(X_2d[:, 0], X_2d[:, 1], c=y, cmap=cmap_pts, edgecolors='k', s=30, linewidths=0.5)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('特征1', fontsize=9)
    ax.set_ylabel('特征2', fontsize=9)

    # 添加图例
    handles, _ = scatter.legend_elements()
    n_classes = len(np.unique(y))
    class_labels = ['类别 {}'.format(i) for i in range(n_classes)]
    ax.legend(handles, class_labels, loc='upper right', fontsize=8)

    plt.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

@compare_tool_bp.route('/')
def compare_home():
    """对比器首页"""
    return render_template('compare_tool/home.html',
                           datasets=COMPARE_DATASETS,
                           algorithms=COMPARE_ALGORITHMS)

@compare_tool_bp.route('/run', methods=['POST'])
def compare_run():
    """执行对比 - 接收JSON返回结果"""
    from sklearn.model_selection import cross_val_score, train_test_split
    import numpy as np

    data = request.json
    dataset_key = data.get('dataset', 'iris')
    algo_keys = data.get('algorithms', ['knn', 'dt', 'svm'])

    # 加载数据
    X, y, X_2d, names = _load_dataset(dataset_key)
    if X is None:
        return jsonify({'error': '数据集不存在'}), 400

    results = []
    for algo_key in algo_keys:
        if algo_key not in COMPARE_ALGORITHMS:
            continue

        algo_info = COMPARE_ALGORITHMS[algo_key]
        params = dict(algo_info['params'])

        # 训练并计时
        clf = _get_classifier(algo_key, params)
        if clf is None:
            continue

        # 5折交叉验证
        start = time.time()
        scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
        cv_time = time.time() - start

        # 训练完整模型用于决策边界
        start = time.time()
        clf.fit(X_2d, y)
        train_time = time.time() - start

        # 决策边界图
        boundary_img = _plot_decision_boundary(clf, X_2d, y, algo_info['name'])

        results.append({
            'key': algo_key,
            'name': algo_info['name'],
            'icon': algo_info['icon'],
            'desc': algo_info['desc'],
            'accuracy_mean': round(float(scores.mean()) * 100, 1),
            'accuracy_std': round(float(scores.std()) * 100, 1),
            'cv_time': round(cv_time, 3),
            'train_time': round(train_time, 4),
            'boundary_img': boundary_img,
            'params': params,
        })

    # 按准确率排序
    results.sort(key=lambda r: r['accuracy_mean'], reverse=True)

    return jsonify({
        'dataset': COMPARE_DATASETS[dataset_key]['name'],
        'dataset_key': dataset_key,
        'results': results,
        'samples': int(X.shape[0]),
        'features': int(X.shape[1]),
        'classes': int(len(np.unique(y))),
    })
