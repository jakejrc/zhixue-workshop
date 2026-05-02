# -*- coding: utf-8 -*-
"""学习工具蓝图 - 期末考试、复习卡片、数据集、Python指南、课程笔记"""
import json, random
from flask import Blueprint, render_template, request, jsonify, session
from data.exam_data import EXAM_POOL
from data.study_data import FLASHCARDS, DATASETS

study_bp = Blueprint('study', __name__, url_prefix='/study')

# ==================== 期末模拟考试 ====================

@study_bp.route('/exam/')
def exam_home():
    """考试首页 - 选择考试参数"""
    return render_template('study/exam_home.html')

@study_bp.route('/exam/start')
def exam_start():
    """开始考试 - 随机抽题"""
    count = request.args.get('count', 30, type=int)
    chapters = request.args.get('chapters', '')
    count = min(count, len(EXAM_POOL))

    if chapters:
        ch_list = [int(c) for c in chapters.split(',')]
        pool = [q for q in EXAM_POOL if q['chapter'] in ch_list]
    else:
        pool = list(EXAM_POOL)

    if len(pool) < count:
        count = len(pool)

    selected = random.sample(pool, count)
    # 存入session
    session['exam_questions'] = selected
    session['exam_answers'] = {}
    return render_template('study/exam_run.html', questions=selected, count=count)

@study_bp.route('/exam/check', methods=['POST'])
def exam_check():
    """检查单题答案"""
    data = request.json
    idx = data.get('index', 0)
    answer = data.get('answer', -1)
    questions = session.get('exam_questions', [])
    if idx < len(questions):
        q = questions[idx]
        correct = answer == q['answer']
        # 记录答案
        if 'exam_answers' not in session:
            session['exam_answers'] = {}
        session['exam_answers'][str(idx)] = answer
        session.modified = True
        return jsonify({'correct': correct, 'answer': q['answer'], 'explanation': q.get('explanation', '')})
    return jsonify({'error': '题目不存在'}), 404

@study_bp.route('/exam/result')
def exam_result():
    """考试结果"""
    questions = session.get('exam_questions', [])
    answers = session.get('exam_answers', {})
    correct = 0
    details = []
    for i, q in enumerate(questions):
        user_ans = answers.get(str(i), -1)
        is_correct = user_ans == q['answer']
        if is_correct:
            correct += 1
        details.append({
            'question': q['q'],
            'options': q['options'],
            'user_answer': user_ans,
            'correct_answer': q['answer'],
            'is_correct': is_correct,
            'explanation': q.get('explanation', ''),
            'chapter': q['chapter'],
        })
    total = len(questions)
    score = round(correct / total * 100) if total > 0 else 0
    return render_template('study/exam_result.html', details=details, correct=correct, total=total, score=score)

# ==================== 复习卡片 ====================

@study_bp.route('/flashcards/')
def flashcard_list():
    """卡片列表 - 选章节"""
    return render_template('study/flashcard_list.html', flashcards=FLASHCARDS)

@study_bp.route('/flashcards/<int:chapter_id>')
def flashcard_study(chapter_id):
    """学习某章卡片"""
    if chapter_id not in FLASHCARDS:
        return '章节不存在', 404
    data = FLASHCARDS[chapter_id]
    return render_template('study/flashcard_study.html', chapter_id=chapter_id, data=data)

# ==================== 数据集下载 ====================

@study_bp.route('/datasets/')
def dataset_list():
    """数据集列表"""
    return render_template('study/datasets.html', datasets=DATASETS)

# ==================== Python环境指南 ====================

@study_bp.route('/python-guide/')
def python_guide():
    """Python环境安装指南"""
    return render_template('study/python_guide.html')

# ==================== 课程笔记 ====================

@study_bp.route('/notes/')
def notes_page():
    """课程笔记页面"""
    return render_template('study/notes.html')
