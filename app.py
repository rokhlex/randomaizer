from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

choices = []

@app.route('/')
def index():
    return render_template('index.html', choices=choices)

@app.route('/random')
def random_choice():
    if choices:
        random_choice = random.choice(choices)
        return render_template('result.html', choice=random_choice)
    else:
        flash('Список вариантов пуст. Пожалуйста, добавьте варианты!', 'warning')
        return redirect(url_for('index'))

@app.route('/clear', methods=['GET'])
def clear_choices():
    global choices
    choices = []
    flash('Все варианты удалены!', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)