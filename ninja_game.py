from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'shhHello'
import random

@app.route('/')
def index():
    if 'activity' not in session:
        session['activity'] = []
    if 'count_gold' not in session:
        session['count_gold'] = 0
    return render_template('index.html')

@app.route('/process1', methods=['POST'])
def farm_process():
    if 'f_gold' not in session:
        session['f_gold'] = 0
    session['f_gold'] = random.randrange(10,20)
    session['count_gold'] += session['f_gold']
    session['activity'].append('Ninja gets {} gold!'.format(session['f_gold']))
    return redirect('/')

@app.route('/process2', methods=['POST'])
def cave_process():
    if 'c_gold' not in session:
        session['c_gold'] = 0
    session['c_gold'] = random.randrange(5,10)
    session['count_gold'] += session['c_gold']
    session['activity'].append('Ninja gets {} gold!'.format(session['c_gold']))
    return redirect('/')

@app.route('/process3', methods=['POST'])
def house_process():
    if 'h_gold' not in session:
        session['h_gold'] = 0
    session['h_gold'] = random.randrange(15,25)
    session['count_gold'] += session['h_gold']
    session['activity'].append('Ninja gets {} gold!'.format(session['h_gold']))
    return redirect('/')

@app.route('/process4', methods=['POST'])
def casino_process():
    if 'cas_gold' not in session:
        session['cas_gold'] = 0
    x = random.randrange(0,9)
    if x > 5:
        session['cas_gold'] = random.randrange(5,50)
        session['count_gold'] += session['cas_gold']
        session['activity'].append('Ninja gets {} gold!'.format(session['cas_gold']))
    elif x <= 5:
        session['cas_gold'] = random.randrange(5,50)
        session['count_gold'] -= session['cas_gold']
        session['activity'].append('Ninja loses {} gold!'.format(session['cas_gold']))
    return redirect('/')
app.run(debug=True)