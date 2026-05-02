"""测验数据"""

QUIZZES = {
    1: {
        'title': '第1章 机器学习概述',
        'questions': [
            {
                'question': '以下哪项不属于机器学习的三大学习范式？',
                'options': ['有监督学习', '无监督学习', '强化学习', '半监督学习'],
                'answer': 2,
                'explanation': '机器学习三大学习范式为：有监督学习、无监督学习、半监督学习。强化学习是另一类学习方式，但不在本课程的三大学习范式分类中。'
            },
            {
                'question': '机器学习的通用流程，正确的顺序是？',
                'options': ['特征工程→数据准备→模型训练→性能度量', '目标分析→数据准备→特征工程→模型训练→性能度量→模型部署', '数据准备→模型训练→目标分析→性能度量', '模型训练→数据准备→特征工程→性能度量'],
                'answer': 1,
                'explanation': '标准流程：目标分析→数据准备→特征工程→模型训练→性能度量→模型部署。'
            },
            {
                'question': '以下哪个是有监督学习的典型算法？',
                'options': ['K-Means', 'PCA', '线性回归', 'DBSCAN'],
                'answer': 2,
                'explanation': '线性回归是有监督学习算法，需要带标签的训练数据。K-Means、PCA、DBSCAN都是无监督学习算法。'
            },
            {
                'question': 'scikit-learn主要用于什么？',
                'options': ['深度学习', '机器学习算法实现', '数据采集', '网页开发'],
                'answer': 1,
                'explanation': 'scikit-learn是Python最常用的机器学习库，提供分类、回归、聚类等算法实现。'
            },
            {
                'question': '以下哪个不是机器学习的典型应用领域？',
                'options': ['金融风控', '医疗诊断', '操作系统内核开发', '电商推荐'],
                'answer': 2,
                'explanation': '操作系统内核开发属于系统软件工程，不是机器学习的典型应用领域。'
            },
        ]
    },
    2: {
        'title': '第2章 数据准备',
        'questions': [
            {
                'question': 'MCAR代表什么含义？',
                'options': ['最大相关分析', '完全随机缺失', '多分类回归', '矩阵分解'],
                'answer': 1,
                'explanation': 'MCAR（Missing Completely At Random）表示缺失与任何变量无关，是最理想的缺失类型。'
            },
            {
                'question': '使用IQR准则检测异常值，正常数据范围是？',
                'options': ['Q1 ~ Q3', 'Q1-1.5×IQR ~ Q3+1.5×IQR', '均值±2倍标准差', '最小值 ~ 最大值'],
                'answer': 1,
                'explanation': 'IQR准则：正常范围为 [Q1-1.5×IQR, Q3+1.5×IQR]，超出此范围的为异常值。'
            },
            {
                'question': '以下哪个不是描述集中趋势的统计量？',
                'options': ['均值', '中位数', '标准差', '众数'],
                'answer': 2,
                'explanation': '标准差描述的是数据的离散程度，不是集中趋势。均值、中位数、众数才是集中趋势的度量。'
            },
            {
                'question': '缺失值处理中，"前值插补"适用于什么场景？',
                'options': ['完全随机缺失', '时间序列数据', '分类变量', '高维数据'],
                'answer': 1,
                'explanation': '前值插补（用前一个非缺失值填充）适用于时间序列数据，因为相邻时间点的数据通常相近。'
            },
            {
                'question': '3σ原则中，异常值的判定标准是？',
                'options': ['超过均值±1倍标准差', '超过均值±2倍标准差', '超过均值±3倍标准差', '超过均值±4倍标准差'],
                'answer': 2,
                'explanation': '3σ原则：超过均值±3倍标准差的数据点被视为异常值，约99.7%的正常数据在此范围内。'
            },
        ]
    },
    3: {
        'title': '第3章 特征工程',
        'questions': [
            {
                'question': 'Min-Max标准化的结果范围是？',
                'options': ['[-1, 1]', '[0, 1]', '[-∞, +∞]', '[0, +∞]'],
                'answer': 1,
                'explanation': 'Min-Max标准化公式 x\'=(x-min)/(max-min)，将数据映射到[0,1]区间。'
            },
            {
                'question': 'Z-Score标准化的特点是？',
                'options': ['映射到[0,1]', '均值为0，标准差为1', '映射到[-1,1]', '保留原始分布'],
                'answer': 1,
                'explanation': 'Z-Score标准化公式 x\'=(x-μ)/σ，结果的均值为0，标准差为1。'
            },
            {
                'question': '独热编码(One-Hot Encoding)的作用是？',
                'options': ['数据归一化', '将离散特征转换为二进制向量', '特征降维', '异常值处理'],
                'answer': 1,
                'explanation': '独热编码将离散型特征转换为二进制向量，如颜色"红/绿/蓝"→[1,0,0],[0,1,0],[0,0,1]。'
            },
            {
                'question': 'Lasso特征选择属于哪种类型？',
                'options': ['过滤式', '包裹式', '嵌入式', '稀疏编码'],
                'answer': 2,
                'explanation': 'Lasso使用L1正则化，在模型训练过程中自动完成特征选择，属于嵌入式方法。'
            },
            {
                'question': 'RFE代表什么？',
                'options': ['随机特征提取', '递归特征消除', '正则化特征评估', '鲁棒特征编码'],
                'answer': 1,
                'explanation': 'RFE（Recursive Feature Elimination）递归特征消除，属于包裹式特征选择方法。'
            },
        ]
    },
    4: {
        'title': '第4章 有监督学习',
        'questions': [
            {
                'question': '精确率(Precision)的计算公式是？',
                'options': ['TP/(TP+FN)', 'TP/(TP+FP)', '(TP+TN)/Total', '2×P×R/(P+R)'],
                'answer': 1,
                'explanation': 'Precision = TP/(TP+FP)，关注"预测为正的样本中有多少真正为正"。'
            },
            {
                'question': 'kNN算法属于什么类型的算法？',
                'options': ['急切学习', '懒惰学习', '增量学习', '在线学习'],
                'answer': 1,
                'explanation': 'kNN是懒惰学习的代表，训练阶段不做任何计算，预测时才计算距离。'
            },
            {
                'question': '决策树CART算法使用什么作为划分准则？',
                'options': ['信息增益', '信息增益率', '基尼指数', '熵'],
                'answer': 2,
                'explanation': 'CART算法使用基尼指数作为划分准则，可用于分类和回归。'
            },
            {
                'question': 'SVM中核技巧的作用是？',
                'options': ['加速训练', '将数据隐式映射到高维空间', '减少特征数量', '处理缺失值'],
                'answer': 1,
                'explanation': '核技巧通过核函数将数据隐式映射到高维空间，使线性不可分的数据变得线性可分。'
            },
            {
                'question': '随机森林属于什么集成策略？',
                'options': ['Boosting', 'Bagging', 'Stacking', 'Blending'],
                'answer': 1,
                'explanation': '随机森林基于Bagging策略，并行训练多个决策树基学习器，通过投票/平均减少方差。'
            },
            {
                'question': '朴素贝叶斯的"朴素"体现在什么假设上？',
                'options': ['线性关系假设', '条件独立性假设', '正态分布假设', '同方差性假设'],
                'answer': 1,
                'explanation': '朴素贝叶斯假设各特征之间条件独立，即P(x|c) = ∏P(xi|c)，这个假设是"朴素"的由来。'
            },
        ]
    },
    5: {
        'title': '第5章 无监督学习',
        'questions': [
            {
                'question': 'PCA降维时，通常选择主成分的标准是？',
                'options': ['特征数量的一半', '累计贡献率达到80%-90%', '固定选3个', '与类别数相同'],
                'answer': 1,
                'explanation': 'PCA选择前m个主成分使得累计贡献率达到80%-90%，即可实现有效降维。'
            },
            {
                'question': 'K-Means算法的缺点不包括？',
                'options': ['需要预设k值', '对初始中心敏感', '能发现任意形状的簇', '假设簇为凸形'],
                'answer': 2,
                'explanation': 'K-Means假设簇为凸形（球形），不能发现任意形状的簇，这是它的缺点。DBSCAN才能发现任意形状的簇。'
            },
            {
                'question': 'DBSCAN中，核心对象的定义是？',
                'options': ['距离最近的点', 'ε邻域内样本数≥MinPts的点', '密度最大的点', '聚类中心点'],
                'answer': 1,
                'explanation': '核心对象：以该点为中心、ε为半径的邻域内，样本数不少于MinPts。'
            },
            {
                'question': '以下哪个是聚类的内部评估指标？',
                'options': ['Jaccard系数', 'Rand指数', 'DBI（越小越好）', 'F1值'],
                'answer': 2,
                'explanation': 'DBI（Davies-Bouldin指数）是内部指标，不需要参考标签，值越小表示聚类效果越好。'
            },
            {
                'question': '层次聚类的聚集法是？',
                'options': ['自顶向下', '自底向上', '随机分裂', '迭代优化'],
                'answer': 1,
                'explanation': '层次聚类的聚集法（Agglomerative）是自底向上，每对簇按最短/最长/平均距离合并。'
            },
        ]
    },
    6: {
        'title': '第6章 智能推荐',
        'questions': [
            {
                'question': '关联规则中，支持度的定义是？',
                'options': ['P(B|A)', 'P(A∩B)', 'P(A|B)', 'P(A)×P(B)'],
                'answer': 1,
                'explanation': '支持度 = P(A∩B)，表示A和B同时出现的概率。'
            },
            {
                'question': '协同过滤中，"基于用户"的核心思想是？',
                'options': ['推荐最热门的物品', '找到兴趣相似的邻居用户', '分析物品内容相似度', '使用标签匹配'],
                'answer': 1,
                'explanation': '基于用户的协同过滤：找到与目标用户兴趣相似的邻居用户，推荐邻居喜欢的物品。'
            },
            {
                'question': '冷启动问题指的是？',
                'options': ['系统启动慢', '新用户/新物品无历史数据', '算法收敛慢', '数据量太大'],
                'answer': 1,
                'explanation': '冷启动问题是指新用户或新物品没有历史行为数据，无法使用协同过滤等方法进行推荐。'
            },
            {
                'question': 'FP-Growth相比Apriori的优势是？',
                'options': ['更准确', '只需两次数据集扫描，效率更高', '不需要支持度', '可以处理连续值'],
                'answer': 1,
                'explanation': 'FP-Growth构建FP-Tree，只需两次数据集扫描，通过条件模式基递归挖掘，效率优于Apriori。'
            },
        ]
    },
    7: {
        'title': '第7章 逻辑回归',
        'questions': [
            {
                'question': '逻辑回归中使用的激活函数是？',
                'options': ['ReLU', 'Sigmoid', 'Tanh', 'Softmax'],
                'answer': 1,
                'explanation': '逻辑回归使用Sigmoid函数将线性输出映射到(0,1)区间，表示概率。'
            },
            {
                'question': '逻辑回归的损失函数是？',
                'options': ['均方误差', '交叉熵损失', 'Hinge损失', '指数损失'],
                'answer': 1,
                'explanation': '逻辑回归使用交叉熵损失（对数损失），通过最大似然估计推导得出。'
            },
            {
                'question': '逻辑回归主要用于什么任务？',
                'options': ['回归', '分类', '聚类', '降维'],
                'answer': 1,
                'explanation': '虽然名字含"回归"，但逻辑回归是分类算法，输出类别概率。'
            },
            {
                'question': 'Softmax回归是逻辑回归的什么推广？',
                'options': ['二分类到多分类', '线性到非线性', '有监督到无监督', '分类到回归'],
                'answer': 0,
                'explanation': 'Softmax回归（多项逻辑回归）将二分类的逻辑回归推广到多分类场景。'
            },
            {
                'question': '逻辑回归对特征的要求是？',
                'options': ['必须是数值型', '可以是任意类型', '需要特征独立', '需要线性可分'],
                'answer': 0,
                'explanation': '逻辑回归需要数值型特征输入，分类特征需要编码转换。'
            },
        ]
    },
    8: {
        'title': '第8章 支持向量机',
        'questions': [
            {
                'question': 'SVM的核心思想是？',
                'options': ['最小化训练误差', '最大化分类间隔', '最小化模型复杂度', '最大化似然函数'],
                'answer': 1,
                'explanation': 'SVM通过找到最大间隔的超平面来分类，间隔越大泛化能力越强。'
            },
            {
                'question': '以下哪个不是常用的核函数？',
                'options': ['线性核', '多项式核', 'RBF核', 'Sigmoid激活函数'],
                'answer': 3,
                'explanation': '常用核函数包括线性核、多项式核、RBF（高斯）核。Sigmoid是激活函数不是核函数。'
            },
            {
                'question': '软间隔SVM中C参数的作用是？',
                'options': ['控制核函数宽度', '控制误分类惩罚程度', '控制学习率', '控制迭代次数'],
                'answer': 1,
                'explanation': 'C越大对误分类惩罚越重，间隔越小；C越小允许更多误分类，间隔越大。'
            },
            {
                'question': 'SVM在高维空间中表现好的原因是？',
                'options': ['计算速度快', '核技巧避免维度灾难', '不需要调参', '自动特征选择'],
                'answer': 1,
                'explanation': '核技巧可以在低维空间计算高维空间的内积，避免了直接在高维空间运算。'
            },
            {
                'question': 'RBF核的gamma参数越大，模型会？',
                'options': ['越简单', '越复杂', '不变', '无法训练'],
                'answer': 1,
                'explanation': 'gamma越大，每个支持向量影响范围越小，决策边界越复杂，容易过拟合。'
            },
        ]
    },
    9: {
        'title': '第9章 朴素贝叶斯',
        'questions': [
            {
                'question': '朴素贝叶斯的"朴素"指什么假设？',
                'options': ['数据线性可分', '特征条件独立', '数据正态分布', '类别均衡'],
                'answer': 1,
                'explanation': '"朴素"指假设给定类别后各特征之间相互独立，这是朴素贝叶斯的核心假设。'
            },
            {
                'question': '拉普拉斯平滑的作用是？',
                'options': ['加速训练', '防止零概率', '减少过拟合', '增加特征'],
                'answer': 1,
                'explanation': '拉普拉斯平滑给每个计数加1，避免某个特征值在训练集中未出现导致概率为0。'
            },
            {
                'question': '高斯朴素贝叶斯假设特征服从什么分布？',
                'options': ['均匀分布', '正态分布', '泊松分布', '指数分布'],
                'answer': 1,
                'explanation': '高斯朴素贝叶斯假设每个特征在给定类别下服从正态分布。'
            },
            {
                'question': '朴素贝叶斯的优点不包括？',
                'options': ['训练速度快', '适合高维数据', '特征独立假设总是成立', '适合文本分类'],
                'answer': 2,
                'explanation': '特征独立假设在现实中往往不成立，但朴素贝叶斯仍然在很多场景表现良好。'
            },
            {
                'question': '朴素贝叶斯在以下哪个领域应用最广泛？',
                'options': ['图像识别', '垃圾邮件过滤', '语音识别', '自动驾驶'],
                'answer': 1,
                'explanation': '朴素贝叶斯在文本分类（尤其是垃圾邮件过滤）中应用最广泛且效果好。'
            },
        ]
    },
    10: {
        'title': '第10章 神经网络',
        'questions': [
            {
                'question': '神经网络中激活函数的作用是？',
                'options': ['加速计算', '引入非线性', '减少参数', '防止过拟合'],
                'answer': 1,
                'explanation': '激活函数引入非线性，使神经网络能够学习复杂的非线性映射关系。'
            },
            {
                'question': '反向传播算法用于什么？',
                'options': ['前向计算', '计算梯度更新权重', '数据预处理', '网络结构设计'],
                'answer': 1,
                'explanation': '反向传播通过链式法则从输出层向输入层逐层计算梯度，用于更新网络权重。'
            },
            {
                'question': '以下哪个不是常用的激活函数？',
                'options': ['ReLU', 'Sigmoid', 'Tanh', 'PCA'],
                'answer': 3,
                'explanation': 'PCA是降维方法，不是激活函数。常用激活函数包括ReLU、Sigmoid、Tanh等。'
            },
            {
                'question': '过拟合的解决方法不包括？',
                'options': ['Dropout', '正则化', '增加训练数据', '增加网络层数'],
                'answer': 3,
                'explanation': '增加网络层数会增加模型复杂度，可能加重过拟合。Dropout、正则化、增加数据都是防过拟合方法。'
            },
            {
                'question': 'ReLU函数的表达式是？',
                'options': ['max(0, x)', '1/(1+e^-x)', '(e^x-e^-x)/(e^x+e^-x)', 'x/(1+|x|)'],
                'answer': 0,
                'explanation': 'ReLU(x) = max(0, x)，即负数输出0，正数输出原值。'
            },
        ]
    },
    11: {
        'title': '第11章 监督学习练习',
        'questions': [
            {
                'question': '高光谱图像分类的典型流程第一步是？',
                'options': ['模型训练', '数据加载与预处理', '特征选择', '模型评估'],
                'answer': 1,
                'explanation': '标准流程：数据加载→缺失值/异常值处理→归一化→降噪→降维→特征提取→分类→评估。'
            },
            {
                'question': '波士顿房价预测中，R²值越接近什么表示模型越好？',
                'options': ['0', '0.5', '1', '-1'],
                'answer': 2,
                'explanation': 'R²（决定系数）越接近1表示模型拟合效果越好，接近0表示模型无预测能力。'
            },
            {
                'question': 'TipDM平台的特点是？',
                'options': ['纯代码操作', '拖曳式数据分析', '只能处理文本', '需要安装本地软件'],
                'answer': 1,
                'explanation': 'TipDM是基于Python引擎的开源拖曳式数据分析平台，支持无编程基础用户使用。'
            },
        ]
    },
    12: {
        'title': '第12章 无监督学习练习',
        'questions': [
            {
                'question': 'Iris数据集的类别数是？',
                'options': ['2', '3', '4', '5'],
                'answer': 1,
                'explanation': 'Iris（鸢尾花）数据集有3个类别：Setosa、Versicolour、Virginica，每类50个样本。'
            },
            {
                'question': 't-SNE主要用于什么？',
                'options': ['分类', '回归', '高维数据可视化', '特征选择'],
                'answer': 2,
                'explanation': 't-SNE是一种非线性降维方法，主要用于高维数据的可视化，将数据降到2维或3维。'
            },
            {
                'question': 'Calinski-Harabasz指数（CH指数）的特点是？',
                'options': ['越小越好', '越大越好', '固定为1', '与k值无关'],
                'answer': 1,
                'explanation': 'CH指数衡量簇内紧密度和簇间分离度，值越大表示聚类效果越好。'
            },
        ]
    },
    13: {
        'title': '第13章 期末考试',
        'questions': [
            {
                'question': '期末上机考试使用的数据集是？',
                'options': ['Iris数据集', '波士顿房价数据集', 'Raw_500.xlsx高光谱数据集', 'MNIST数据集'],
                'answer': 2,
                'explanation': '期末上机考试统一使用Raw_500.xlsx高光谱数据集，构建农药残留识别模型。'
            },
            {
                'question': '大数据3班的特征工程方法是？',
                'options': ['标准化+SG平滑', '归一化+MSC降噪', 'PCA降维', 'LDA降维'],
                'answer': 1,
                'explanation': '大数据3班：归一化+MSC降噪→PCA→SVM+决策树；大数据2班：标准化+SG平滑→LDA→逻辑回归+随机森林。'
            },
            {
                'question': '评估指标不包括以下哪个？',
                'options': ['Accuracy', 'Precision', 'Recall', 'AUC-ROC'],
                'answer': 3,
                'explanation': '期末考试评估指标为：Accuracy / Precision / Recall / F1 / 混淆矩阵，不包括AUC-ROC。'
            },
        ]
    },
}
