from flask import Flask, render_template, request, abort, session

# create instance of Flask class 
# __name__ is special python variable related to name of app
app = Flask(__name__)

@app.route('/')
def simple_add():
    return render_template('simple_add.html')

@app.route('/result', methods=['POST'])
def add_result():
    sum = int(request.form['num1']) + int(request.form['num2'])
    if(sum > 9223372036854775807 or
        sum < -9223372036854775808-1 ):
        abort(400)
    return render_template(
        'add_result.html',
        sum=sum)