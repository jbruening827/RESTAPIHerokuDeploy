from app113 import app
from db113 import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()