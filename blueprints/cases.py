from flask import Blueprint, render_template
from data.cases_data import CASES

cases_bp = Blueprint('cases', __name__)

@cases_bp.route('/')
def case_list():
    return render_template('cases/list.html', cases=CASES)

@cases_bp.route('/<case_key>')
def case_detail(case_key):
    case = CASES.get(case_key)
    if not case:
        from flask import abort
        abort(404)
    return render_template('cases/detail.html', case=case, case_key=case_key, cases=CASES)
