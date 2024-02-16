from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path, mkdir

ARTICLE_DB = 'article_database'
EMAIL_SUBSCRIPTION_DB_NAME = 'email_subscriptions'

DATABASES_DIR = 'databases'
UPLOAD_DIR = 'website/static/assets/'
SECRET_KEY = 'secret-key'


def create_database(app, database):
    if not path.exists(path.join('website', DATABASES_DIR)):
        mkdir(path.join('website', DATABASES_DIR))

    if not path.exists(path.join('website', ARTICLE_DB + '.db')):
        database.create_all(app=app)

    for db_name in app.config['SQLALCHEMY_BINDS']:
        db_path = path.join('website', DATABASES_DIR, db_name, '.db')
        if not path.exists(db_path):
            database.create_all(bind=db_name)


def create_dir():
    required_dirs = {'article_covers', 'event_covers', 'volunteer_covers'}
    for directory in required_dirs:
        if not path.exists(UPLOAD_DIR + directory):
            mkdir(UPLOAD_DIR + directory)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite://{ARTICLE_DB}.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_BINDS'] = {
        'email_subscriptions': f'sqlite:///{DATABASES_DIR}/{EMAIL_SUBSCRIPTION_DB_NAME}.db',
    }

    app.config['UPLOAD_DIR'] = UPLOAD_DIR
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    # Assign db and migrate to app
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # Initialize db
    db.init_app(app)

    # Register blueprints
    from .views import views
    from .errorhandler import errorhandler_mold

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(errorhandler_mold, url_prefix='/error-pages')

    # Create databases
    create_database(app, db)

    # Create directories
    create_dir()

    return app
