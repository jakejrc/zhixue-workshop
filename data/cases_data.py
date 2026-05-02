"""综合案例数据"""

CASES = {
    'fiscal_revenue': {
        'name': '市财政收入预测',
        'chapter': 7,
        'icon': 'bi-graph-up',
        'color': '#6f42c1',
        'summary': '基于某市1994-2013年财政收入历史数据，利用Lasso特征选择+灰色预测+SVR组合方法，预测2014和2015年财政收入。',
        'steps': [
            {
                'title': '数据准备与Pearson相关分析',
                'desc': '分析13个特征与财政收入的相关性。发现x11（居民消费价格指数）与y不相关，其余高度正相关，但特征间存在严重共线性。',
                'code': 'import pandas as pd\nimport numpy as np\n\n# 加载数据\ndf = pd.read_csv("fiscal_data.csv")\n\n# Pearson相关系数矩阵\ncorr_matrix = df.corr()\nprint(corr_matrix["y"].sort_values(ascending=False))',
            },
            {
                'title': 'Lasso特征选择',
                'desc': '通过L1正则化将不重要特征系数压缩为0，筛选出8个关键特征（x1, x3, x4, x5, x7, x8, x9, x13）。',
                'code': 'from sklearn.linear_model import Lasso\n\nlasso = Lasso(alpha=0.1)\nlasso.fit(X_train, y_train)\n\n# 查看特征系数\nfeature_importance = pd.Series(lasso.coef_, index=feature_names)\nselected = feature_importance[feature_importance != 0]\nprint("Selected features:", selected.index.tolist())',
            },
            {
                'title': '灰色预测GM(1,1)',
                'desc': '对关键特征进行时间序列预测，经过后验差检验精度等级为"好"。',
                'code': 'def gm11_predict(data, predict_num=2):\n    """GM(1,1)灰色预测"""\n    x0 = np.array(data)\n    x1 = np.cumsum(x0)  # 累加生成\n    z1 = (x1[:-1] + x1[1:]) / 2  # 紧邻均值\n    \n    # 最小二乘求参数\n    B = np.column_stack((-z1, np.ones(len(z1))))\n    Y = x0[1:]\n    u = np.linalg.inv(B.T @ B) @ B.T @ Y\n    a, b = u[0], u[1]\n    \n    # 预测\n    result = []\n    for k in range(len(x0) + predict_num):\n        result.append((x0[0] - b/a) * np.exp(-a*k) + b/a)\n    return np.diff(result)[-predict_num:]',
            },
            {
                'title': 'SVR支持向量回归',
                'desc': '使用SVR模型进行回归预测，R方值0.991，模型拟合效果优良。预测2014年2187.18亿元、2015年2538.09亿元。',
                'code': 'from sklearn.svm import SVR\nfrom sklearn.metrics import r2_score\n\nsvr = SVR(kernel="rbf", C=100, gamma=0.1)\nsvr.fit(X_train, y_train)\n\ny_pred = svr.predict(X_test)\nprint(f"R² = {r2_score(y_test, y_pred):.3f}")\n# R² = 0.991\n\n# 预测2014-2015年\nfuture_pred = svr.predict(X_future)\nprint(f"2014年预测: {future_pred[0]:.2f}亿元")\nprint(f"2015年预测: {future_pred[1]:.2f}亿元")',
            },
        ],
        'result': 'SVR模型R²=0.991，预测2014年财政收入2187.18亿元，2015年2538.09亿元。Lasso有效去除共线性特征，灰色预测补充时间序列趋势。',
    },
    'power_monitoring': {
        'name': '非侵入式电力负荷监测',
        'chapter': 8,
        'icon': 'bi-lightning',
        'color': '#ffc107',
        'summary': '利用NILM技术，从入户总功率数据中分解出各设备数据，基于kNN算法实现11种家电设备的识别分类。',
        'steps': [
            {
                'title': '数据探索与可视化',
                'desc': '对11种设备（风扇、微波炉、热水壶、笔记本电脑等）的电流、电压、功率特征进行折线图可视化分析。',
                'code': 'import matplotlib.pyplot as plt\nimport pandas as pd\n\n# 加载11种设备数据\ndevices = ["fan", "microwave", "kettle", "laptop", \n           "incandescent", "led", "printer", \n           "water_dispenser", "ac", "hair_dryer", "tv"]\n\nfor device in devices:\n    df = pd.read_csv(f"data/{device}.csv")\n    plt.plot(df["power"], label=device)\nplt.legend()\nplt.title("11种设备功率特征")\nplt.show()',
            },
            {
                'title': '特征构造',
                'desc': '设备数据选取无功功率、总无功功率、有功功率、总有功功率、功率因数、总功率因数6个特征。',
                'code': '# 构造特征\nfeatures = ["reactive_power", "total_reactive", \n            "active_power", "total_active",\n            "power_factor", "total_pf"]\n\nX = df[features]\ny = df["device_label"]',
            },
            {
                'title': '缺失值处理与kNN建模',
                'desc': '大缺失段删除，小缺失段前值插补。使用kNN算法进行设备识别分类。',
                'code': 'from sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import accuracy_score\n\n# 缺失值处理\ndf = df.dropna(thresh=len(features)-1)  # 大段缺失删除\ndf = df.fillna(method="ffill")  # 小段前值插补\n\n# kNN建模\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)\nknn = KNeighborsClassifier(n_neighbors=5)\nknn.fit(X_train, y_train)\n\nprint(f"设备识别准确率: {accuracy_score(y_test, knn.predict(X_test)):.2%}")',
            },
            {
                'title': '实时用电量计算',
                'desc': '根据识别出的设备类型和功率，计算实时用电量：W = P×100/3600，P = U×I。',
                'code': '# 实时用电量计算\ndef calc_energy(voltage, current, time_seconds):\n    power = voltage * current  # P = U×I (W)\n    energy = power * time_seconds / 3600  # Wh\n    return energy\n\n# 示例：220V, 1A设备运行1小时\nenergy = calc_energy(220, 1, 3600)\nprint(f"用电量: {energy:.2f} Wh = {energy/1000:.3f} kWh")',
            },
        ],
        'result': 'kNN算法成功识别11种家电设备，通过功率特征可准确判断设备类型，实现非侵入式负荷监测。',
    },
    'airline': {
        'name': '航空公司客户价值分析',
        'chapter': 9,
        'icon': 'bi-people',
        'color': '#20c997',
        'summary': '基于RFM模型改进为LRFMC模型，利用K-Means聚类对客户进行分群，识别高价值客户并制定差异化营销策略。',
        'steps': [
            {
                'title': '数据清洗',
                'desc': '删除缺失值和异常值，确保数据质量。',
                'code': 'import pandas as pd\nimport numpy as np\n\n# 加载数据\ndf = pd.read_csv("airline_data.csv")\n\n# 删除缺失值\ndf = df.dropna()\n\n# 异常值处理 (IQR方法)\nfor col in ["FFP_INTERVAL", "LAST_TO_END", "FLIGHT_COUNT", "SEG_KM_SUM", "avg_discount"]:\n    Q1, Q3 = df[col].quantile([0.25, 0.75])\n    IQR = Q3 - Q1\n    df = df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]',
            },
            {
                'title': 'LRFMC特征构造',
                'desc': '将RFM模型扩展为LRFMC：客户关系长度L、时间间隔R、消费频率F、飞行里程M、折扣系数C。',
                'code': '# LRFMC特征构造\ndf["L"] = (pd.to_datetime("2014-03-31") - pd.to_datetime(df["FFP_DATE"])).dt.days / 30\ndf["R"] = df["LAST_TO_END"]  # 最后一次乘机间隔(月)\ndf["F"] = df["FLIGHT_COUNT"]  # 飞行次数\ndf["M"] = df["SEG_KM_SUM"]    # 总飞行公里数\ndf["C"] = df["avg_discount"]  # 平均折扣率\n\nlrfmc = df[["L", "R", "F", "M", "C"]]\nprint(lrfmc.describe())',
            },
            {
                'title': '数据标准化',
                'desc': '对LRFMC特征进行Z-Score标准化。',
                'code': 'from sklearn.preprocessing import StandardScaler\n\nscaler = StandardScaler()\nlrfmc_scaled = scaler.fit_transform(lrfmc)\nlrfmc_scaled = pd.DataFrame(lrfmc_scaled, columns=["L","R","F","M","C"])\nprint(lrfmc_scaled.head())',
            },
            {
                'title': 'K-Means聚类（CH指数确定k=4）',
                'desc': '使用CH指数评估不同k值，确定最优聚类数为4。',
                'code': 'from sklearn.cluster import KMeans\nfrom sklearn.metrics import calinski_harabasz_score\n\n# 用CH指数选择k\nch_scores = []\nfor k in range(2, 8):\n    km = KMeans(n_clusters=k, random_state=42)\n    labels = km.fit_predict(lrfmc_scaled)\n    ch = calinski_harabasz_score(lrfmc_scaled, labels)\n    ch_scores.append((k, ch))\n    print(f"k={k}, CH={ch:.0f}")\n\n# 最优k=4\nbest_k = max(ch_scores, key=lambda x: x[1])[0]\nprint(f"最优k = {best_k}")',
            },
            {
                'title': '客户价值分析与营销策略',
                'desc': '分析4个客户群的LRFMC特征，制定差异化营销策略。',
                'code': '# 聚类结果分析\nkm = KMeans(n_clusters=4, random_state=42)\ndf["cluster"] = km.fit_predict(lrfmc_scaled)\n\n# 各簇中心分析\ncenters = pd.DataFrame(km.cluster_centers_, columns=["L","R","F","M","C"])\nprint("各客户群特征:")\nprint(centers)\n\n# 客户群分布\nprint("\\n客户群人数分布:")\nprint(df["cluster"].value_counts().sort_index())\n# 客户群0: 5563 - 重要保持客户\n# 客户群1: 12939 - 一般客户\n# 客户群2: 17253 - 重要挽留客户\n# 客户群3: 26288 - 低价值客户',
            },
        ],
        'result': 'CH指数确定k=4，识别出重要保持客户(5563人)、一般客户(12939人)、重要挽留客户(17253人)、低价值客户(26288人)四类，制定差异化营销策略。',
    },
    'broadcasting': {
        'name': '广电大数据营销推荐',
        'chapter': 10,
        'icon': 'bi-tv',
        'color': '#6610f2',
        'summary': '基于广电2000名用户数据，构建用户画像，结合协同过滤+TF-IDF+流行度混合推荐实现精准营销。',
        'steps': [
            {
                'title': '数据清洗',
                'desc': '去除特殊线路和政企用户，收视记录去重、隔夜分割、短时观看(<4秒)删除。',
                'code': 'import pandas as pd\n\n# 加载5类数据\nviewing = pd.read_csv("viewing_records.csv")  # 收视行为\nbills = pd.read_csv("bills.csv")              # 账单\norders = pd.read_csv("orders.csv")            # 订单\n\n# 数据清洗\nviewing = viewing[viewing["duration"] >= 4]     # 删除短时观看\nviewing = viewing.drop_duplicates()             # 去重\nviewing = viewing[~viewing["user_type"].isin(["special", "enterprise"])]',
            },
            {
                'title': '用户画像标签体系（3大类20+标签）',
                'desc': '构建基本特征(5项)、业务特征(11项)、兴趣爱好(4项)的标签体系。',
                'code': '# 用户画像构建\nuser_profile = pd.DataFrame()\n\n# 基本特征\nuser_profile["family_size"] = user_data["family_members"]\nuser_profile["payment_method"] = user_data["pay_type"]\n\n# 业务特征\nuser_profile["tv_dependency"] = viewing.groupby("user_id")["duration"].mean()\nuser_profile["loyalty"] = orders.groupby("user_id")["months_active"].mean()\n\n# 兴趣偏好\ngenre_cols = ["sports", "finance", "life", "movie", "variety", "drama", "education", "news"]\nfor genre in genre_cols:\n    user_profile[f"prefer_{genre}"] = viewing.groupby("user_id")[genre].sum()',
            },
            {
                'title': '混合推荐模型',
                'desc': '并行组合三种推荐：物品协同过滤(个性化)、TF-IDF标签推荐(冷启动)、流行度推荐(新用户)。',
                'code': 'from sklearn.metrics.pairwise import cosine_similarity\nimport numpy as np\n\n# 1. 基于物品的协同过滤\nitem_sim = cosine_similarity(item_features.T)  # 物品相似度矩阵\ndef item_cf_recommend(user_id, top_n=10):\n    user_items = get_user_items(user_id)\n    scores = item_sim[user_items].mean(axis=0)\n    return np.argsort(scores)[::-1][:top_n]\n\n# 2. TF-IDF标签推荐 (解决冷启动)\nfrom sklearn.feature_extraction.text import TfidfVectorizer\ntfidf = TfidfVectorizer()\ntag_features = tfidf.fit_transform(program_tags)\ndef tag_recommend(user_tags, top_n=10):\n    user_vec = tfidf.transform([user_tags])\n    sim = cosine_similarity(user_vec, tag_features)\n    return np.argsort(sim[0])[::-1][:top_n]\n\n# 3. 流行度推荐\ndef popular_recommend(top_n=10):\n    return viewing["program_id"].value_counts().head(top_n).index.tolist()',
            },
            {
                'title': '营销建议生成',
                'desc': '根据用户画像和推荐结果，生成个性化营销策略。',
                'code': '# 营销策略\ndef generate_strategy(user_profile):\n    strategies = []\n    \n    # 家庭用户\n    if user_profile["family_size"] > 2:\n        strategies.append("推荐家庭套餐，含儿童+老人节目")\n    \n    # 独居青年\n    if user_profile["family_size"] == 1 and user_profile["age"] < 35:\n        strategies.append("推荐个性化点播套餐")\n    \n    # 高消费用户\n    if user_profile["monthly_bill"] > 200:\n        strategies.append("推荐VIP尊享服务")\n    \n    # 低活跃用户\n    if user_profile["tv_dependency"] < 30:\n        strategies.append("推送热门节目，提升活跃度")\n    \n    return strategies',
            },
        ],
        'result': '构建2000+用户画像，混合推荐系统覆盖个性化推荐、冷启动和新用户场景，营销策略实现精准触达。',
    },
}
