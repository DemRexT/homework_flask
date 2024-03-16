from flask import Flask, render_template

app = Flask(__name__)


html = """
<h1>Это моя первая страница Html</h1>
<p>Привет, мир!</p>
"""

_users = [{'name': 'Ivan',
'Last_name': 'Ivanov',
'age': '44',
'average_mark': '4.8',
},
{'name': 'Ivan',
'Last_name': 'Ivanov',
'age': '44',
'average_mark': '4.8',
},]



@app.route('/')
def HelloWorld():
    return 'Hello world'

@app.route('/about/')
def about():
    return 'about.html'

@app.route('/contact/')
def contact():
    return 'contact.html'

@app.route('/number/<int:num1>/<int:num2>/')
def sum(num1, num2):
    return str(num1 + num2)

@app.route('/strlen/<stroka>/')
def strlen(stroka):
    return str(len(stroka))

@app.route('/web/')
def web():
    return html

@app.route('/table/')
def table():
    return render_template('table.html', users = _users)

if __name__ == '__main__':
    app.run(debug=True)