"""算法可视化数据"""

ALGORITHMS = {
    'knn': {
        'name': 'k近邻分类 (kNN)',
        'category': 'supervised',
        'chapter': 4,
        'description': 'kNN是最简单的分类算法之一：找到k个最近的邻居，投票决定类别。',
        'formula': '距离: d(x,y) = √Σ(xi-yi)²',
        'key_points': [
            '懒惰学习：训练阶段无计算，预测时才计算距离',
            'k值选择：k太小过拟合，k太大欠拟合',
            '距离度量：欧氏距离、曼哈顿距离等',
            '需要特征缩放，否则大数值特征主导距离',
        ],
        'params': [
            {'name': 'k', 'type': 'range', 'min': 1, 'max': 15, 'default': 3, 'step': 2},
        ],
    },
    'kmeans': {
        'name': 'K-Means聚类',
        'category': 'unsupervised',
        'chapter': 5,
        'description': 'K-Means是最常用的聚类算法：随机初始化k个中心，迭代优化。',
        'formula': '目标: min Σ Σ ||x - μi||²',
        'key_points': [
            '需要预先指定k值',
            '迭代过程：分配样本→更新中心→收敛',
            '对初始中心敏感，常用K-Means++',
            '假设簇为凸形，不适用非凸形状',
        ],
        'params': [
            {'name': 'k', 'type': 'range', 'min': 2, 'max': 8, 'default': 3, 'step': 1},
        ],
    },
    'linear_regression': {
        'name': '线性回归',
        'category': 'supervised',
        'chapter': 4,
        'description': '线性回归是最基础的回归算法：拟合一条直线使残差平方和最小。',
        'formula': 'w* = (X^TX)^{-1}X^Ty',
        'key_points': [
            '最小二乘法：最小化残差平方和',
            '假设特征与目标之间存在线性关系',
            '多元线性回归扩展到多变量',
            '可通过正则化（Ridge/Lasso）防止过拟合',
        ],
        'params': [],
    },
    'decision_tree': {
        'name': '决策树',
        'category': 'supervised',
        'chapter': 4,
        'description': '决策树通过一系列if-else规则进行分类或回归，可解释性强。',
        'formula': 'ID3: 信息增益 | C4.5: 信息增益率 | CART: 基尼指数',
        'key_points': [
            'ID3：信息增益，偏向取值多的特征',
            'C4.5：信息增益率，克服ID3的偏向',
            'CART：基尼指数，可用于分类和回归',
            '容易过拟合，需要剪枝',
        ],
        'params': [
            {'name': 'max_depth', 'type': 'range', 'min': 1, 'max': 10, 'default': 3, 'step': 1},
        ],
    },
    'svm': {
        'name': '支持向量机 (SVM)',
        'category': 'supervised',
        'chapter': 4,
        'description': 'SVM寻找最优超平面使异类样本间隔最大化，核技巧处理非线性问题。',
        'formula': 'max margin = 2/||w||',
        'key_points': [
            '核心：最大化分类间隔',
            '核技巧：线性/多项式/RBF/拉普拉斯核',
            '软间隔：引入松弛变量容忍错误',
            'SMO算法高效求解',
        ],
        'params': [
            {'name': 'C', 'type': 'range', 'min': 0.1, 'max': 10, 'default': 1, 'step': 0.1},
        ],
    },
    'pca': {
        'name': '主成分分析 (PCA)',
        'category': 'unsupervised',
        'chapter': 5,
        'description': 'PCA通过线性变换将高维数据投影到低维，保留最大方差方向。',
        'formula': 'y = T^Tx (T为特征向量矩阵)',
        'key_points': [
            '选择累计贡献率80%-90%的主成分',
            '新变量是原始变量的正交线性组合',
            '降维同时去除噪声和冗余',
            'KPCA通过核函数处理非线性数据',
        ],
        'params': [
            {'name': 'n_components', 'type': 'range', 'min': 1, 'max': 5, 'default': 2, 'step': 1},
        ],
    },
    'dbscan': {
        'name': 'DBSCAN密度聚类',
        'category': 'unsupervised',
        'chapter': 5,
        'description': 'DBSCAN基于样本密度进行聚类，能发现任意形状的簇并识别噪声点。',
        'formula': '核心对象: |Nε(p)| ≥ MinPts',
        'key_points': [
            '核心对象：ε邻域内样本数≥MinPts',
            '密度直达→密度可达→密度相联',
            '能发现任意形状的簇',
            '自动识别噪声点',
        ],
        'params': [
            {'name': 'eps', 'type': 'range', 'min': 0.1, 'max': 2.0, 'default': 0.5, 'step': 0.1},
            {'name': 'min_samples', 'type': 'range', 'min': 2, 'max': 10, 'default': 5, 'step': 1},
        ],
    },
    'naive_bayes': {
        'name': '朴素贝叶斯',
        'category': 'supervised',
        'chapter': 4,
        'description': '基于贝叶斯定理和条件独立性假设，计算简单高效，适合文本分类。',
        'formula': 'P(c|x) = P(x|c) × P(c) / P(x)',
        'key_points': [
            '条件独立性假设：P(x|c) = ∏ P(xi|c)',
            '拉普拉斯平滑解决零概率问题',
            '计算简单高效',
            '特别适合高维文本分类',
        ],
        'params': [],
    },
}
