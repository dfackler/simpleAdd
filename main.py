from flask import Flask, render_template, request, abort, session
import operator

# create instance of Flask class 
# __name__ is special python variable related to name of app
app = Flask(__name__)

@app.route('/')
def simple_add():
    return render_template('simple_add.html')

@app.route('/result', methods=['POST'])
def add_result():
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq,
           '+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           'X': operator.mul,
           '/': operator.div,
           '%': operator.div,
           '^': operator.pow,
           '**': operator.pow}
    result = ops[request.form['operation']](int(request.form['num1']), int(request.form['num2']))
    return render_template(
        'add_result.html',
        sum=result)