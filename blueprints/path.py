# -*- coding: utf-8 -*-
"""学习路径推荐蓝图"""
from flask import Blueprint, render_template
from data.chapters_data import CHAPTERS
from data.path_data import CHAPTER_DEPS, LEARNING_PATHS, CHAPTER_HOURS, CHAPTER_DIFFICULTY

# 转成字典方便模板访问
CHAPTERS_DICT = {ch['id']: ch for ch in CHAPTERS}

path_bp = Blueprint('path', __name__, url_prefix='/path')

@path_bp.route('/')
def path_home():
    """学习路径推荐页面"""
    return render_template('path/path.html',
                           chapters=CHAPTERS_DICT,
                           deps=CHAPTER_DEPS,
                           paths=LEARNING_PATHS,
                           hours=CHAPTER_HOURS,
                           difficulty=CHAPTER_DIFFICULTY)
