# -*- coding: utf-8 -*-
"""期末考试题库 - 从13章抽取，每章10-15题"""

EXAM_POOL = [
    # ---- 第1章 机器学习概述 ----
    {'chapter': 1, 'q': '机器学习的核心思想是？', 'options': ['人工编写规则', '从数据中自动学习规律', '穷举所有可能', '模拟人脑神经元'], 'answer': 1, 'explanation': '机器学习通过算法从数据中自动发现规律，而非人工编写规则。'},
    {'chapter': 1, 'q': '以下哪项属于无监督学习？', 'options': ['垃圾邮件分类', '房价预测', '客户聚类', '图像识别'], 'answer': 2, 'explanation': '聚类没有标签，属于无监督学习；分类和回归属于有监督学习。'},
    {'chapter': 1, 'q': '机器学习通用流程的正确顺序是？', 'options': ['模型训练→数据准备→特征工程', '数据准备→特征工程→模型训练', '特征工程→数据准备→模型训练', '数据准备→模型训练→特征工程'], 'answer': 1, 'explanation': '标准流程：数据准备→特征工程→模型训练→评估→部署。'},
    {'chapter': 1, 'q': 'scikit-learn主要用于？', 'options': ['深度学习', '数据可视化', '传统机器学习算法', '大数据处理'], 'answer': 2, 'explanation': 'sklearn专注于传统ML算法，深度学习用TensorFlow/PyTorch。'},
    {'chapter': 1, 'q': '以下哪个不是机器学习的应用领域？', 'options': ['图像识别', '自然语言处理', '编译原理', '推荐系统'], 'answer': 2, 'explanation': '编译原理属于计算机科学基础，不是ML应用领域。'},

    # ---- 第2章 数据准备 ----
    {'chapter': 2, 'q': 'MCAR指的是？', 'options': ['完全随机缺失', '随机缺失', '非随机缺失', '无缺失'], 'answer': 0, 'explanation': 'MCAR(Missing Completely At Random)：缺失与任何变量无关。'},
    {'chapter': 2, 'q': 'IQR准则判断异常值的标准是？', 'options': ['超出均值±2σ', '超出Q1-1.5×IQR或Q3+1.5×IQR', '超出中位数±1.5', '超出极差的80%'], 'answer': 1, 'explanation': 'IQR=Q3-Q1，超出[Q1-1.5×IQR, Q3+1.5×IQR]的值为异常值。'},
    {'chapter': 2, 'q': '以下哪种方法不适合处理缺失值？', 'options': ['均值填充', '删除缺失行', '中位数填充', '直接忽略该列全部数据'], 'answer': 3, 'explanation': '直接丢弃整列数据会造成信息损失，不是合理的缺失值处理方法。'},
    {'chapter': 2, 'q': '描述性统计中，衡量数据离散程度的指标是？', 'options': ['均值', '中位数', '标准差', '众数'], 'answer': 2, 'explanation': '标准差衡量数据的离散程度；均值/中位数/众数衡量集中趋势。'},
    {'chapter': 2, 'q': '数据标准化的主要目的是？', 'options': ['增加数据量', '消除量纲差异', '减少特征数量', '增加缺失值'], 'answer': 1, 'explanation': '标准化将不同量纲的特征缩放到同一尺度。'},

    # ---- 第3章 特征工程 ----
    {'chapter': 3, 'q': 'Min-Max标准化的结果范围是？', 'options': ['[-1, 1]', '[0, 1]', '[-∞, +∞]', '[0, +∞]'], 'answer': 1, 'explanation': 'Min-Max将数据线性缩放到[0,1]区间。'},
    {'chapter': 3, 'q': '独热编码(One-Hot Encoding)适用于？', 'options': ['连续特征', '有序特征', '无序离散特征', '文本特征'], 'answer': 2, 'explanation': '独热编码将无序离散特征转为二进制向量。'},
    {'chapter': 3, 'q': 'Lasso回归使用哪种正则化？', 'options': ['L1正则化', 'L2正则化', 'L1+L2混合', '无正则化'], 'answer': 0, 'explanation': 'Lasso使用L1正则化，可将部分特征系数压缩为0，实现特征选择。'},
    {'chapter': 3, 'q': 'RFE属于哪种特征选择方法？', 'options': ['过滤式', '包裹式', '嵌入式', '降维式'], 'answer': 1, 'explanation': 'RFE(递归特征消除)通过反复训练模型来评估特征重要性，属于包裹式。'},
    {'chapter': 3, 'q': 'Z-Score标准化后的数据特点是？', 'options': ['范围在[0,1]', '均值为0，标准差为1', '范围在[-1,1]', '中位数为0'], 'answer': 1, 'explanation': 'Z-Score标准化使数据均值为0、标准差为1。'},

    # ---- 第4章 有监督学习 ----
    {'chapter': 4, 'q': '线性回归使用什么方法求解参数？', 'options': ['梯度下降', '最小二乘法', '最大似然估计', '贝叶斯估计'], 'answer': 1, 'explanation': '线性回归通过最小二乘法最小化残差平方和求解参数。'},
    {'chapter': 4, 'q': 'kNN算法中，k值过小会导致？', 'options': ['欠拟合', '过拟合', '无影响', '训练加速'], 'answer': 1, 'explanation': 'k值过小，模型对噪声敏感，容易过拟合。'},
    {'chapter': 4, 'q': 'SVM的核技巧用于处理？', 'options': ['缺失值', '高维数据', '非线性分类', '大规模数据'], 'answer': 2, 'explanation': '核技巧将数据映射到高维空间，使非线性问题变为线性可分。'},
    {'chapter': 4, 'q': '决策树CART算法使用什么指标划分节点？', 'options': ['信息增益', '信息增益率', '基尼指数', '熵'], 'answer': 2, 'explanation': 'CART算法使用基尼指数(Gini Index)选择最优划分。'},
    {'chapter': 4, 'q': '逻辑回归的输出经过什么函数变换？', 'options': ['ReLU', 'Sigmoid', 'Tanh', 'Softmax'], 'answer': 1, 'explanation': '逻辑回归通过Sigmoid函数将输出映射到[0,1]概率区间。'},
    {'chapter': 4, 'q': '随机森林属于什么类型的集成方法？', 'options': ['Bagging', 'Boosting', 'Stacking', 'Blending'], 'answer': 0, 'explanation': '随机森林是Bagging的代表算法，通过多棵决策树投票。'},
    {'chapter': 4, 'q': '朴素贝叶斯的"朴素"指的是？', 'options': ['算法简单', '特征条件独立', '不需要训练', '只用于二分类'], 'answer': 1, 'explanation': '"朴素"假设各特征之间相互独立，这在现实中往往不成立但效果仍好。'},

    # ---- 第5章 无监督学习 ----
    {'chapter': 5, 'q': 'PCA降维的核心思想是？', 'options': ['删除不重要的特征', '找到最大方差方向投影', '聚类后取中心', '随机选择特征'], 'answer': 1, 'explanation': 'PCA通过找到数据方差最大的方向(主成分)进行投影降维。'},
    {'chapter': 5, 'q': 'K-Means算法的k值通常用什么方法确定？', 'options': ['随机选择', '肘部法则', '交叉验证', '网格搜索'], 'answer': 1, 'explanation': '肘部法则通过观察SSE下降拐点确定最优k值。'},
    {'chapter': 5, 'q': 'DBSCAN相比K-Means的优势是？', 'options': ['速度更快', '能发现任意形状的簇', '不需要参数', '总是更好的结果'], 'answer': 1, 'explanation': 'DBSCAN基于密度，能发现非球形簇并自动识别噪声点。'},
    {'chapter': 5, 'q': 'PCA选择主成分数量时，累计贡献率通常取？', 'options': ['50%-60%', '60%-70%', '80%-90%', '100%'], 'answer': 2, 'explanation': '通常选择累计贡献率达到80%-90%的主成分数量。'},
    {'chapter': 5, 'q': '层次聚类的结果通常用什么展示？', 'options': ['散点图', '树状图', '折线图', '饼图'], 'answer': 1, 'explanation': '层次聚类通过树状图(Dendrogram)展示聚类合并过程。'},

    # ---- 第6章 智能推荐 ----
    {'chapter': 6, 'q': '关联规则中，支持度衡量的是？', 'options': ['规则的准确性', '项集同时出现的概率', '规则的覆盖率', '项集的独立性'], 'answer': 1, 'explanation': '支持度=P(A∩B)，衡量A和B同时出现的概率。'},
    {'chapter': 6, 'q': '协同过滤的冷启动问题是指？', 'options': ['算法启动慢', '新用户/新物品缺少数据', '计算资源不足', '数据量太大'], 'answer': 1, 'explanation': '冷启动指新用户或新物品缺少历史数据，无法进行推荐。'},
    {'chapter': 6, 'q': 'ItemCF的核心思想是？', 'options': ['找相似用户', '找相似物品', '推荐最热门的', '随机推荐'], 'answer': 1, 'explanation': 'ItemCF通过物品相似度，推荐与用户历史喜好相似的物品。'},
    {'chapter': 6, 'q': 'TF-IDF中，IDF的作用是？', 'options': ['提高常见词权重', '降低常见词权重', '增加文本长度', '减少特征数量'], 'answer': 1, 'explanation': 'IDF(逆文档频率)降低在所有文档中都出现的常见词的权重。'},
    {'chapter': 6, 'q': 'Apriori算法利用什么性质减少搜索空间？', 'options': ['对称性', '反单调性', '单调性', '传递性'], 'answer': 1, 'explanation': '反单调性：如果项集非频繁，其超集也一定非频繁。'},

    # ---- 第7章 案例：财政收入 ----
    {'chapter': 7, 'q': '财政收入预测案例中，特征选择使用的方法是？', 'options': ['PCA', 'Lasso', 'RFE', '随机森林'], 'answer': 1, 'explanation': '案例使用Lasso回归的L1正则化进行特征选择。'},
    {'chapter': 7, 'q': 'GM(1,1)灰色预测模型适用于？', 'options': ['大样本数据', '小样本时间序列', '图像数据', '文本数据'], 'answer': 1, 'explanation': '灰色预测适用于小样本、贫信息的时间序列预测。'},
    {'chapter': 7, 'q': 'SVR是SVM在什么任务上的扩展？', 'options': ['分类', '回归', '聚类', '降维'], 'answer': 1, 'explanation': 'SVR(Support Vector Regression)是SVM用于回归任务的变体。'},

    # ---- 第8章 案例：电力负荷 ----
    {'chapter': 8, 'q': 'NILM的全称是？', 'options': ['非侵入式负荷监测', '网络智能学习模型', '新型增量学习方法', '自然语言逻辑模型'], 'answer': 0, 'explanation': 'NILM = Non-Intrusive Load Monitoring，从总功率分解各设备用电。'},
    {'chapter': 8, 'q': '电力负荷监测案例使用的分类算法是？', 'options': ['SVM', 'kNN', '决策树', '朴素贝叶斯'], 'answer': 1, 'explanation': '案例使用kNN算法识别11种家电设备。'},

    # ---- 第9章 案例：航空客户 ----
    {'chapter': 9, 'q': 'LRFMC模型中的L代表？', 'options': ['消费金额', '客户关系长度', '最近一次消费', '消费频率'], 'answer': 1, 'explanation': 'L=Length，客户关系长度，即会员入会时长。'},
    {'chapter': 9, 'q': '航空公司客户价值案例中，确定聚类数k的方法是？', 'options': ['肘部法则', 'CH指数', '轮廓系数', '手肘法+CH指数'], 'answer': 3, 'explanation': '案例综合使用肘部法则和CH指数确定k=4。'},

    # ---- 第10章 案例：广电营销 ----
    {'chapter': 10, 'q': '广电营销案例中，解决冷启动问题使用的方法是？', 'options': ['随机推荐', 'TF-IDF标签推荐', '深度学习', '人工标注'], 'answer': 1, 'explanation': '案例使用TF-IDF对节目标签进行文本分析，构建标签推荐模型。'},
    {'chapter': 10, 'q': '混合推荐系统的优势是？', 'options': ['计算更快', '可以互补单一方法的不足', '不需要数据', '总是准确'], 'answer': 1, 'explanation': '混合推荐结合多种方法，弥补单一方法的局限性。'},

    # ---- 第11章 监督学习练习 ----
    {'chapter': 11, 'q': '高光谱数据降维常用的方法是？', 'options': ['PCA', 'K-Means', 'DBSCAN', 'Apriori'], 'answer': 0, 'explanation': '高光谱数据维度极高(数百波段)，PCA是最常用的降维方法。'},
    {'chapter': 11, 'q': '房价预测评估中，R²接近1表示？', 'options': ['模型很差', '模型拟合很好', '数据有误', '过拟合'], 'answer': 1, 'explanation': 'R²(决定系数)越接近1，说明模型对数据的解释能力越强。'},
    {'chapter': 11, 'q': 'LDA在分类任务中的作用是？', 'options': ['特征缩放', '降维+分类', '聚类', '异常检测'], 'answer': 1, 'explanation': 'LDA(线性判别分析)既是降维方法，也用于分类。'},

    # ---- 第12章 无监督学习练习 ----
    {'chapter': 12, 'q': 'CH指数越高表示？', 'options': ['聚类效果越差', '聚类效果越好', '数据量越大', '特征越多'], 'answer': 1, 'explanation': 'CH指数越高，说明簇间分离度越大、簇内紧凑度越好。'},
    {'chapter': 12, 'q': 't-SNE主要用于？', 'options': ['分类', '回归', '高维数据可视化', '推荐'], 'answer': 2, 'explanation': 't-SNE是非线性降维方法，主要用于高维数据的2D/3D可视化。'},

    # ---- 第13章 期末考试 ----
    {'chapter': 13, 'q': '以下哪个算法既可以用于分类又可以用于回归？', 'options': ['K-Means', '决策树', 'PCA', 'Apriori'], 'answer': 1, 'explanation': '决策树既可以做分类(CART分类树)也可以做回归(CART回归树)。'},
    {'chapter': 13, 'q': '过拟合的典型表现是？', 'options': ['训练集和测试集表现都差', '训练集表现好但测试集差', '训练集差但测试集好', '两者表现一样'], 'answer': 1, 'explanation': '过拟合：模型在训练集上学得太好，泛化能力差，测试集表现差。'},
    {'chapter': 13, 'q': '交叉验证的主要目的是？', 'options': ['增加训练数据', '更可靠地评估模型', '加速训练', '减少特征'], 'answer': 1, 'explanation': '交叉验证通过多次划分训练/测试集，给出更稳定的模型评估结果。'},
    {'chapter': 13, 'q': '以下哪种方法可以缓解过拟合？', 'options': ['增加特征', '增加数据量', '减少正则化', '增加模型复杂度'], 'answer': 1, 'explanation': '增加数据量、增加正则化、减少模型复杂度都可以缓解过拟合。'},
    {'chapter': 13, 'q': '集成学习中，Bagging和Boosting的主要区别是？', 'options': ['Bagging串行训练，并行训练', 'Bagging并行训练，Boosting串行训练', '没有区别', 'Bagging用于回归，Boosting用于分类'], 'answer': 1, 'explanation': 'Bagging(如随机森林)并行训练多个独立模型；Boosting(如GBDT)串行训练，后一个修正前一个的错误。'},
]
