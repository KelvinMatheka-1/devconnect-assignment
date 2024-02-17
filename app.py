import config
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@localhost/test_database'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    date_created  = db.Column(db.DateTime, default=datetime.utcnow)
    # completed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Task {self.id}>"
    
@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue adding task"
        
    else:
      tasks = Todo.query.order_by(Todo.date_created).all()
      print(tasks)
      return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue deleting the task"
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating the task"
    else:
        return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
