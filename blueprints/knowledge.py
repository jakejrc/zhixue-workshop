from flask import Blueprint, render_template, request, jsonify
from data.knowledge_data import CHAPTER_DEPS, CHAPTER_NODES, COMPARISONS, FORMULAS
from data.chapters_data import CHAPTERS
from data.algorithms_data import ALGORITHMS
from data.cases_data import CASES
from data.quiz_data import QUIZZES

knowledge_bp = Blueprint('knowledge', __name__, url_prefix='/knowledge')
compare_bp = Blueprint('compare', __name__, url_prefix='/compare')
formula_bp = Blueprint('formula', __name__, url_prefix='/formula')
search_bp = Blueprint('search', __name__, url_prefix='/search')


@knowledge_bp.route('/')
def graph():
    return render_template('knowledge/graph.html',
                           nodes=CHAPTER_NODES,
                           deps=CHAPTER_DEPS)


@compare_bp.route('/')
def compare_list():
    return render_template('compare/list.html', comparisons=COMPARISONS)


@compare_bp.route('/<comp_id>')
def compare_detail(comp_id):
    comp = next((c for c in COMPARISONS if c['id'] == comp_id), None)
    if not comp:
        return "Not found", 404
    return render_template('compare/detail.html', comp=comp, all_comps=COMPARISONS)


@formula_bp.route('/')
def formula_list():
    return render_template('formula/list.html', formulas=FORMULAS)


@formula_bp.route('/<formula_id>')
def formula_detail(formula_id):
    formula = next((f for f in FORMULAS if f['id'] == formula_id), None)
    if not formula:
        return "Not found", 404
    return render_template('formula/detail.html', formula=formula, all_formulas=FORMULAS)


@search_bp.route('/')
def search_page():
    q = request.args.get('q', '').strip()
    results = []
    if q:
        q_lower = q.lower()
        # 搜索章节
        for ch in CHAPTERS:
            title = ch.get('title', '') or ch.get('name', '')
            desc = ch.get('summary', '') or ch.get('desc', '')
            kc = ch.get('key_concepts', '')
            kc_text = ''
            if isinstance(kc, list):
                kc_text = ' '.join(k.get('name', '') for k in kc)
            elif isinstance(kc, str):
                kc_text = kc
            if q_lower in title.lower() or q_lower in desc.lower() or q_lower in kc_text.lower():
                results.append({
                    'type': '章节', 'icon': 'bi-book', 'color': '#4e73df',
                    'title': title, 'desc': desc[:80],
                    'url': '/chapters/{}'.format(ch.get('id', ch.get('chapter_id', 1)))
                })
        # 搜索算法
        for akey, algo in ALGORITHMS.items():
            if q_lower in algo['name'].lower() or q_lower in algo.get('description', '').lower():
                results.append({
                    'type': '算法', 'icon': 'bi-bar-chart-line', 'color': '#1cc88a',
                    'title': algo['name'], 'desc': algo.get('description', '')[:80],
                    'url': '/viz/{}'.format(akey)
                })
        # 搜索案例
        for ckey, case in CASES.items():
            if q_lower in case['name'].lower() or q_lower in case.get('summary', '').lower():
                results.append({
                    'type': '案例', 'icon': 'bi-briefcase', 'color': '#e74a3b',
                    'title': case['name'], 'desc': case.get('summary', '')[:80],
                    'url': '/cases/{}'.format(ckey)
                })
        # 搜索对比
        for comp in COMPARISONS:
            if q_lower in comp['title'].lower() or q_lower in comp.get('subtitle', '').lower():
                results.append({
                    'type': '对比', 'icon': 'bi-arrow-left-right', 'color': '#f6c23e',
                    'title': comp['title'], 'desc': comp.get('subtitle', ''),
                    'url': '/compare/{}'.format(comp['id'])
                })
        # 搜索公式
        for f in FORMULAS:
            if q_lower in f['title'].lower() or q_lower in f.get('chapter', '').lower():
                results.append({
                    'type': '公式', 'icon': 'bi-calculator', 'color': '#6f42c1',
                    'title': f['title'], 'desc': f.get('chapter', ''),
                    'url': '/formula/{}'.format(f['id'])
                })
    return render_template('search/results.html', q=q, results=results)
