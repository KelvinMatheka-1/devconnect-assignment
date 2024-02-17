import config
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Use f-string to construct the database URI with credentials from config
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@localhost/test_database'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    date_created  = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"
    
@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            # Add the new task to the database and commit the transaction
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
             # If there's an issue adding the task, display an error message
            return "there was an issue adding task"
        
    else:
      # If it's a GET request, retrieve all tasks and render the template
      tasks = Todo.query.order_by(Todo.date_created).all()
      print(tasks)
      return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        # Delete the task from the database and commit the transaction
        db.session.delete(task_to_delete)
        db.session.commit()

         # Redirect to the homepage to display the updated task list
        return redirect('/')
    except:
        return "There was an issue deleting the task"
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            # Commit the transaction to save the updated task content
            db.session.commit()

            # Redirect to the homepage to display the updated task list
            return redirect('/')
        except:
            return "There was a problem updating the task"
    else:
         # If it's a GET request, render the update form with the task data
        return render_template('update.html', task=task)
    
if __name__ == '__main__':
    app.run(debug=True)
