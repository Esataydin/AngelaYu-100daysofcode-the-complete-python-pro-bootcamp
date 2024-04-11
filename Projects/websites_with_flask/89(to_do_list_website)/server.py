from flask import render_template, redirect, url_for, request

import datetime

from forms import TodoForm
from database import app, db, List


@app.route('/')
def home():
    todos = db.session.query(List).all()[::-1]
    return render_template('index.html', list=todos)


@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
        date = datetime.datetime.now().strftime("%x")
        new_todo = List(
            topic=form.topic.data,
            date=date,
            content=form.content.data,
            is_going=form.is_going.data,
            is_done=form.is_done.data
        )
        with app.app_context():
            db.session.add(new_todo)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/change', methods=['GET', 'PUT'])
def change_todo():
    todo_id = int(request.args.get('todo_id'))
    todo = List.query.get(todo_id)
    if str(request.args.get('action')) == 'going':
        if todo.is_going == True:
            todo.is_going = False
        else:
            todo.is_going = True
    else:
        if todo.is_done == True:
            todo.is_done = False
        else:
            todo.is_done = True
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete', methods=['GET', 'DELETE'])
def delete_todo():
    todo_id = int(request.args.get('todo_id'))
    todo = List.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
