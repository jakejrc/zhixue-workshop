from flask import Blueprint, render_template, request, jsonify, session
from data.tools_data import ALGORITHM_PARAMS, GLOSSARY, LOSS_FUNCTIONS

tools_bp = Blueprint('tools', __name__, url_prefix='/tools')


@tools_bp.route('/params/')
def params_list():
    return render_template('tools/params.html', algorithms=ALGORITHM_PARAMS)


@tools_bp.route('/glossary/')
def glossary():
    q = request.args.get('q', '').strip().lower()
    filtered = GLOSSARY
    if q:
        filtered = [g for g in GLOSSARY if q in g['en'].lower() or q in g['zh'].lower() or q in g['desc'].lower()]
    letters = sorted(set(g['en'][0].upper() for g in GLOSSARY))
    return render_template('tools/glossary.html', glossary=filtered, q=q, letters=letters, total=len(GLOSSARY))


@tools_bp.route('/loss/')
def loss_functions():
    return render_template('tools/loss.html', losses=LOSS_FUNCTIONS)


@tools_bp.route('/evaluation/')
def evaluation():
    return render_template('tools/evaluation.html')


@tools_bp.route('/crossval/')
def crossval():
    return render_template('tools/crossval.html')


@tools_bp.route('/wrongbook/')
def wrongbook():
    wrong_answers = session.get('wrong_answers', {})
    return render_template('tools/wrongbook.html', wrong_answers=wrong_answers)


@tools_bp.route('/wrongbook/add', methods=['POST'])
def wrongbook_add():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error'}), 400
    wrong = session.get('wrong_answers', {})
    key = '{}_{}'.format(data.get('quiz_id', ''), data.get('q_idx', ''))
    if data.get('correct'):
        wrong.pop(key, None)
    else:
        wrong[key] = {
            'quiz_id': data.get('quiz_id'),
            'quiz_title': data.get('quiz_title'),
            'q_idx': data.get('q_idx'),
            'question': data.get('question'),
            'options': data.get('options'),
            'correct': data.get('correct_answer'),
            'chosen': data.get('chosen'),
            'explanation': data.get('explanation'),
        }
    session['wrong_answers'] = wrong
    return jsonify({'status': 'ok', 'count': len(wrong)})


@tools_bp.route('/wrongbook/remove', methods=['POST'])
def wrongbook_remove():
    data = request.get_json()
    key = '{}_{}'.format(data.get('quiz_id', ''), data.get('q_idx', ''))
    wrong = session.get('wrong_answers', {})
    wrong.pop(key, None)
    session['wrong_answers'] = wrong
    return jsonify({'status': 'ok', 'count': len(wrong)})
