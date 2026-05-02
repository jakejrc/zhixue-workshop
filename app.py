"""智学工坊 - 机器学习辅助教学平台"""
from flask import Flask
from blueprints.home import home_bp
from blueprints.chapters import chapters_bp
from blueprints.visualizations import viz_bp
from blueprints.quizzes import quiz_bp
from blueprints.cases import cases_bp
from blueprints.knowledge import knowledge_bp, compare_bp, formula_bp, search_bp
from blueprints.tools import tools_bp
from blueprints.study import study_bp
from blueprints.compare_tool import compare_tool_bp
from blueprints.analyzer import analyzer_bp
from blueprints.path import path_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'zhixue-workshop-2026'

    app.register_blueprint(home_bp)
    app.register_blueprint(chapters_bp, url_prefix='/chapters')
    app.register_blueprint(viz_bp, url_prefix='/viz')
    app.register_blueprint(quiz_bp, url_prefix='/quiz')
    app.register_blueprint(cases_bp, url_prefix='/cases')
    app.register_blueprint(knowledge_bp)
    app.register_blueprint(compare_bp)
    app.register_blueprint(formula_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(tools_bp)
    app.register_blueprint(study_bp)
    app.register_blueprint(compare_tool_bp)
    app.register_blueprint(analyzer_bp)
    app.register_blueprint(path_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
