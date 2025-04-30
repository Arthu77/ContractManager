from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

# 创建主蓝图
from flask import Blueprint
main_bp = Blueprint('main', __name__)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///contracts.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        UPLOAD_FOLDER=os.path.join(app.instance_path, 'uploads')
    )
    
    # 确保实例文件夹存在
    try:
        os.makedirs(app.instance_path)
        os.makedirs(os.path.join(app.instance_path, 'uploads'))
    except OSError:
        pass
    
    db.init_app(app)
    
    from app import routes
    
    with app.app_context():
        db.create_all()
    
    # 注册蓝图
    app.register_blueprint(main_bp)
    
    return app
