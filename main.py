from flask import Flask, render_template, request

# create instance of Flask class 
# __name__ is special python variable related to name of app
app = Flask(__name__)

# create request handler to display form
@app.route('/form')
def form():
    return render_template('form.html')

# create request handler to handle information from form
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)

@app.route('/')
def simple_add():
    return render_template('simple_add.html')

@app.route('/result', methods=['POST'])
def add_result():
    sum = int(request.form['num1']) + int(request.form['num2'])
    return render_template(
        'add_result.html',
        sum=sum)