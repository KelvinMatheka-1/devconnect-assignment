import config
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@localhost/test_database'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String, nullable=False)
    date_created  = db.Column(db.DateTime, default=datetime.utcnow)
    # completed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Task {self.id}>"
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
