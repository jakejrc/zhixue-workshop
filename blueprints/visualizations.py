from flask import Blueprint, render_template
from data.algorithms_data import ALGORITHMS

viz_bp = Blueprint('viz', __name__)

@viz_bp.route('/')
def viz_list():
    return render_template('visualizations/list.html', algorithms=ALGORITHMS)

@viz_bp.route('/<algo_key>')
def viz_detail(algo_key):
    algo = ALGORITHMS.get(algo_key)
    if not algo:
        from flask import abort
        abort(404)
    return render_template('visualizations/detail.html', algo=algo, algo_key=algo_key, algorithms=ALGORITHMS)
