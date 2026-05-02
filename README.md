# 🧠 智学工坊 — 机器学习辅助教学平台

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue.svg" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/Flask-1.1.2-green.svg" alt="Flask 1.1.2">
  <img src="https://img.shields.io/badge/Bootstrap-5.3-purple.svg" alt="Bootstrap 5.3">
  <img src="https://img.shields.io/badge/Chart.js-4.4.0-orange.svg" alt="Chart.js 4.4.0">
  <img src="https://img.shields.io/badge/D3.js-7-red.svg" alt="D3.js 7">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</p>

> **智学工坊**是一个面向高校机器学习课程的交互式辅助教学平台，由[江苏工程职业技术学院](https://www.jseti.edu.cn/)姜荣昌老师设计开发。平台覆盖机器学习课程全部 13 个章节，提供算法可视化、知识图谱、智能测验、学习工具等 30+ 功能模块，帮助学生从"看公式"转变为"动手理解"机器学习。

---

## 📸 平台截图

### 首页
<p align="center">
  <img src="static/screenshots/home.png" width="85%" alt="首页">
</p>

### 课程章节导航
<p align="center">
  <img src="static/screenshots/chapters.png" width="85%" alt="课程章节">
</p>

### 章节详情（知识点 + 代码 + 重点标注）
<p align="center">
  <img src="static/screenshots/chapter_detail.png" width="85%" alt="章节详情">
</p>

### 算法可视化（8 种算法交互演示）
<p align="center">
  <img src="static/screenshots/viz_list.png" width="85%" alt="算法可视化列表">
</p>

<p align="center">
  <img src="static/screenshots/viz_knn.png" width="85%" alt="kNN 可视化">
</p>

### 知识图谱（D3.js 交互式依赖关系）
<p align="center">
  <img src="static/screenshots/knowledge.png" width="85%" alt="知识图谱">
</p>

### 章节测验（65 道题目，即时反馈）
<p align="center">
  <img src="static/screenshots/quiz.png" width="85%" alt="章节测验">
</p>

### 综合案例（真实场景 + 完整代码）
<p align="center">
  <img src="static/screenshots/cases.png" width="85%" alt="综合案例">
</p>

### 模型评估工具（混淆矩阵 / ROC / PR 曲线）
<p align="center">
  <img src="static/screenshots/evaluation.png" width="85%" alt="模型评估">
</p>

### 算法实战对比器（决策边界可视化）
<p align="center">
  <img src="static/screenshots/compare_tool.png" width="85%" alt="算法对比器">
</p>

### 学习路径推荐
<p align="center">
  <img src="static/screenshots/path.png" width="85%" alt="学习路径">
</p>

### 期末模拟考试（限时 + 随机抽题）
<p align="center">
  <img src="static/screenshots/exam.png" width="85%" alt="模拟考试">
</p>

### 课后复习卡片（间隔重复算法）
<p align="center">
  <img src="static/screenshots/flashcards.png" width="85%" alt="复习卡片">
</p>

### 损失函数可视化
<p align="center">
  <img src="static/screenshots/loss.png" width="85%" alt="损失函数">
</p>

---

## ✨ 功能特性

### 📚 课程内容（13 章完整覆盖）

| 章节 | 内容 |
|------|------|
| 第 1 章 | 机器学习概述 |
| 第 2 章 | 线性回归 |
| 第 3 章 | 逻辑回归 |
| 第 4 章 | 朴素贝叶斯 |
| 第 5 章 | 决策树 |
| 第 6 章 | 支持向量机 (SVM) |
| 第 7 章 | 聚类算法 (K-Means / DBSCAN) |
| 第 8 章 | 降维 (PCA) |
| 第 9 章 | 集成学习 |
| 第 10 章 | 神经网络基础 |
| 第 11 章 | 模型评估与选择 |
| 第 12 章 | 特征工程 |
| 第 13 章 | 深度学习简介 |

每章包含：**知识点讲解** + **重点标注** + **代码示例** + **参考资源**

### 🎮 算法可视化（8 种算法交互演示）

在画布上点击添加数据点，实时观察算法运行过程：

| 算法 | 可视化内容 |
|------|-----------|
| kNN | 距离连线 + 邻居高亮 + 分类边界 |
| K-Means | 聚类中心迭代 + Voronoi 区域 |
| 线性回归 | 拟合线 + 残差线 |
| 决策树 | 树结构 + 分裂边界 |
| SVM | 支持向量 + 间隔边界 |
| PCA | 主成分方向 + 投影 |
| DBSCAN | 核心点 / 边界点 / 噪声点 |
| 朴素贝叶斯 | 概率分布 + 决策边界 |

### 🧪 学习工具（10+ 实用工具）

- **算法参数速查表** — 8 种算法的超参数说明与调参建议
- **模型评估可视化** — 混淆矩阵、ROC 曲线、PR 曲线，可调阈值实时更新
- **损失函数可视化** — MSE / MAE / Huber / 交叉熵等 6 种损失函数对比
- **K 折交叉验证动画** — 分步演示数据划分过程
- **错题本** — 自动收集做错的题目，支持重练
- **术语词典** — 200+ 机器学习术语中英对照释义

### 📝 学习管理

- **期末模拟考试** — 限时考试，随机抽题，自动评分
- **课后复习卡片** — 基于间隔重复算法的闪卡复习
- **学习进度追踪** — 本地存储学习进度（无需登录）
- **学习路径推荐** — 基于知识图谱的学习顺序建议
- **薄弱点分析** — 自动分析测验结果，识别薄弱章节
- **错题薄弱点分析** — 按章节统计正确率，推荐复习重点

### 🔍 智能搜索

全文搜索支持：章节标题、知识点、算法名称、术语等

### 📊 知识图谱

D3.js 交互式力导向图，展示 13 个章节的前后置依赖关系

### 🎯 算法实战对比器

选择 2-4 种算法在同一数据集上运行，对比：
- 准确率
- 训练时间
- 决策边界可视化

### 📥 数据集下载

提供 5 个经典机器学习数据集（Iris / Wine / Digits / Boston / Breast Cancer）

---

## 🚀 快速开始

### 环境要求

- Python 3.6+
- pip

### 安装

```bash
# 克隆仓库
git clone https://github.com/jakejrc/zhixue-workshop.git
cd zhixue-workshop

# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
```

或者直接双击 `启动.bat`（Windows）

### 访问

打开浏览器访问 http://localhost:5000

---

## 📁 项目结构

```
zhixue-workshop/
├── app.py                          # Flask 主应用
├── 启动.bat                        # Windows 一键启动脚本
├── requirements.txt                # 依赖：flask
├── blueprints/                     # 蓝图模块
│   ├── home.py                     # 首页
│   ├── chapters.py                 # 课程章节
│   ├── visualizations.py           # 算法可视化
│   ├── quizzes.py                  # 章节测验
│   ├── cases.py                    # 综合案例
│   ├── knowledge.py                # 知识图谱 / 对比 / 公式 / 搜索
│   ├── tools.py                    # 学习工具集
│   ├── study.py                    # 学习管理
│   ├── compare_tool.py             # 算法对比器
│   ├── analyzer.py                 # 薄弱点分析
│   └── path.py                     # 学习路径推荐
├── data/                           # 数据文件
│   ├── chapters_data.py            # 13 章课程内容
│   ├── algorithms_data.py          # 算法参数数据
│   ├── quiz_data.py                # 65 道测验题目
│   ├── cases_data.py               # 综合案例数据
│   ├── knowledge_data.py           # 知识图谱节点与边
│   ├── tools_data.py               # 工具数据（参数表 / 术语）
│   ├── exam_data.py                # 模拟考试题库
│   ├── study_data.py               # 学习资源数据
│   ├── compare_data.py             # 对比器数据集
│   └── path_data.py                # 学习路径数据
├── templates/                      # Jinja2 模板
│   ├── base.html                   # 基础布局（侧边栏导航）
│   ├── home.html                   # 首页
│   ├── chapters/                   # 章节模板
│   ├── visualizations/             # 可视化模板
│   ├── quizzes/                    # 测验模板
│   ├── cases/                      # 案例模板
│   ├── knowledge/                  # 知识图谱模板
│   ├── tools/                      # 工具模板
│   ├── study/                      # 学习管理模板
│   ├── compare_tool/               # 对比器模板
│   ├── analyzer/                   # 分析器模板
│   └── path/                       # 路径模板
└── static/                         # 静态资源
    ├── css/style.css               # 自定义样式
    ├── js/chart.min.js             # Chart.js v4.4.0（本地化）
    └── screenshots/                # 平台截图
```

---

## 🛠️ 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| 后端 | Python 3.6 + Flask 1.1.2 | 轻量级 Web 框架 |
| 模板 | Jinja2 | 服务端渲染 |
| 前端 | Bootstrap 5.3 + 原生 JS | 响应式布局 |
| 图表 | Chart.js 4.4.0（本地化） | ROC/PR 曲线、混淆矩阵 |
| 知识图谱 | D3.js 7 | 交互式力导向图 |
| 算法可视化 | HTML5 Canvas | 实时交互绘图 |
| 存储 | localStorage | 学习进度、错题本、笔记（无需登录） |

---

## 📐 设计理念

1. **零依赖部署** — 仅需 Python + Flask，无需数据库、无需注册登录
2. **交互式学习** — 算法可视化让学生"动手理解"而非"看公式"
3. **知识图谱驱动** — 章节依赖关系可视化，学习路径智能推荐
4. **即时反馈** — 测验即时判分 + 解析，错题自动归集
5. **离线友好** — Chart.js 本地化，不依赖外部 CDN

---

## 📄 License

MIT License

---

---

## 🙏 致谢

- [Flask](https://flask.palletsprojects.com/) — Python Web 框架
- [Bootstrap](https://getbootstrap.com/) — 前端 UI 框架
- [Chart.js](https://www.chartjs.org/) — 图表库
- [D3.js](https://d3js.org/) — 数据可视化库
- [scikit-learn](https://scikit-learn.org/) — 算法灵感来源
