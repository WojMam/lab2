from flask import render_template, flash, redirect, request, url_for
from app import app
import os
from random import choice
from app.forms import LoginForm, svmForm, knnForm, decisionTreeForm, randomForestForm
import algorithms_definitions as ag

@app.route('/')
@app.route('/index')
def index():
    tasks = [
        {
            'number': 'a',
            'content': 'Uzytkownik wybiera zbior danych'
        },
        {
            'number': 'b',
            'content': 'Uzytkownik wybiera algorytm np. kNN'
        },
        {
            'number': 'c',
            'content': 'Uzytkownik moze przypisac wartosci do argumentow wybranego algorytmu'
        },
        {
            'number': 'd',
            'content': 'Po zbudowaniu modelu aplikacja wypisuje wyniki klasyfikacji lacznie z wykresami'
        },
        {
            'number': 'e',
            'content': 'Uzytkownik moze wprowadzic zbior testowy (bez etykiet klas) a aplikacja wypisze predykcje na podstawie zbudowanego modelu.'
        }
    ]
    return render_template('index.html', title='Home', tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/svm', methods=['GET', 'POST'])
def svm():
    form = svmForm()
    if form.validate_on_submit():
        return redirect(url_for('svm_result',form=form))
    img_url = url_for('static', filename=os.path.join('images', 'svm.png'))
    return render_template('svm.html', url =img_url, title='SVM', form=form)

@app.route('/knn', methods=['GET', 'POST'])
def knn():
    form = knnForm()
    if form.validate_on_submit():
        return redirect('/knn_result')
    img_url = url_for('static', filename=os.path.join('images', 'kNN.png'))
    return render_template('knn.html', url =img_url, title='kNN', form=form)

@app.route('/decisiontree', methods=['GET', 'POST'])
def decisiontree():
    form = decisionTreeForm()
    if form.validate_on_submit():
        return redirect('/dt_result')
    img_url = url_for('static', filename=os.path.join('images', 'DecisionTreeClassifier.png'))
    return render_template('decisiontree.html', url =img_url, title='Decision Tree', form=form)

@app.route('/randomforest', methods=['GET', 'POST'])
def randomforest():
    form = randomForestForm()
    if form.validate_on_submit():
        return redirect('/rf_result')
    img_url = url_for('static', filename=os.path.join('images', 'RandomForestClassifier.png'))
    return render_template('randomforest.html', url =img_url, title='Random Forest', form=form)

@app.route('/randomimage', methods=['GET'])
def randomimage():

    names = os.listdir(os.path.join(app.static_folder, 'images'))
    img_url = url_for('static', filename=os.path.join('images', choice(names)))
    return render_template('randomimage.html', url =img_url, title='Random Static Image', img_url=img_url)

@app.route('/svm_result')
def svm_result():
    return render_template('svm_result.html', title='SVM results')

@app.route('/knn_result')
def knn_result():
    return render_template('knn_result.html', title='kNN results', form=request.args.get('form'))

@app.route('/dt_result')
def dt_result():
    return render_template('dt_result.html', title='Decision Tree results')

@app.route('/rf_result')
def rf_result():
    return render_template('rf_result.html', title='Random Forest results')
