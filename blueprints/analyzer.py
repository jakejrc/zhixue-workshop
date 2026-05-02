# -*- coding: utf-8 -*-
"""错题薄弱点分析蓝图 - 分析测验成绩，找出薄弱章节"""
from flask import Blueprint, render_template
from data.chapters_data import CHAPTERS

analyzer_bp = Blueprint('analyzer', __name__, url_prefix='/analyzer')

@analyzer_bp.route('/')
def analyzer_home():
    """薄弱点分析页面 - 数据从localStorage读取"""
    return render_template('analyzer/analyze.html', chapters=CHAPTERS)
