from flask import Blueprint, render_template, request, jsonify, session
from data.quiz_data import QUIZZES

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/')
def quiz_list():
    return render_template('quizzes/list.html', quizzes=QUIZZES)

@quiz_bp.route('/<int:chapter_id>')
def quiz_detail(chapter_id):
    quiz = QUIZZES.get(chapter_id)
    if not quiz:
        from flask import abort
        abort(404)
    return render_template('quizzes/detail.html', quiz=quiz, chapter_id=chapter_id)

@quiz_bp.route('/api/check', methods=['POST'])
def check_answer():
    data = request.get_json()
    chapter_id = data.get('chapter_id')
    q_index = data.get('question_index')
    answer = data.get('answer')
    quiz = QUIZZES.get(chapter_id)
    if not quiz or q_index >= len(quiz['questions']):
        return jsonify({'error': 'Invalid'}), 400
    question = quiz['questions'][q_index]
    correct = answer == question['answer']
    return jsonify({
        'correct': correct,
        'answer': question['answer'],
        'explanation': question.get('explanation', '')
    })
