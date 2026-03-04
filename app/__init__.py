from flask import Flask, render_template
from .database import init_db
from .routes import tasks_bp

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize Database
    init_db(app)
    
    # Register Blueprints
    app.register_blueprint(tasks_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        return render_template('index.html')

    return app
