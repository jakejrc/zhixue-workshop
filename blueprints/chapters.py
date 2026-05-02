from flask import Blueprint, render_template, abort
from data.chapters_data import CHAPTERS

chapters_bp = Blueprint('chapters', __name__)

@chapters_bp.route('/')
def chapter_list():
    return render_template('chapters/list.html', chapters=CHAPTERS)

@chapters_bp.route('/<int:chapter_id>')
def chapter_detail(chapter_id):
    chapter = next((c for c in CHAPTERS if c['id'] == chapter_id), None)
    if not chapter:
        abort(404)
    return render_template('chapters/detail.html', chapter=chapter, chapters=CHAPTERS)
